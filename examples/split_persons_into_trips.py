"""
本文件用于将人的出行拆分为一段一段的Trip（有时候也称为OD）
"""

import argparse
from pymongo import MongoClient
from pycitydata.map import Map
from pycityproto.city.trip.v2 import trip_pb2
from pycityproto.city.routing.v2 import routing_pb2


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mongo_uri", type=str, required=True)
    parser.add_argument("--map_db", type=str, required=True)
    parser.add_argument("--map_coll", type=str, required=True)
    parser.add_argument("--person_db", type=str, required=True)
    parser.add_argument("--person_coll", type=str, required=True)
    parser.add_argument("--output_db", type=str, required=True)
    parser.add_argument("--output_coll", type=str, required=True)
    return parser.parse_args()


def main():
    args = get_args()
    m = Map(args.mongo_uri, args.map_db, args.map_coll, cache_dir="./cache")
    client = MongoClient(args.mongo_uri)
    persons = list(client[args.person_db][args.person_coll].find())
    # 将persons中的schedules中的trips拆出来
    # 记录为(person_id, schedule_i, trip_i, start, start_lnglat, end, end_lnglat)的dict形式
    total_trips = 0
    public_transport_trips = 0 # 公共交通出行
    non_vehicle_trips = 0 # 不是机动化出行的数量
    trips = []
    for person in persons:
        person = person["data"]
        pos = person["home"]
        for i, schedule in enumerate(person["schedules"]):
            for j, trip in enumerate(schedule["trips"]):
                start_xy = m.position2xy(pos)
                end_xy = m.position2xy(trip["end"])
                start_lnglat = m.xy2lnglat(start_xy[0], start_xy[1])
                end_lnglat = m.xy2lnglat(end_xy[0], end_xy[1])
                trips.append(
                    {
                        "id": person["id"],
                        "schedule_i": i,
                        "trip_i": j,
                        "start": pos,
                        "start_lnglat": start_lnglat,
                        "end": trip["end"],
                        "end_lnglat": end_lnglat,
                    }
                )
                total_trips += 1
                if "routes" in trip and len(trip["routes"]) > 0:
                    # 根据routes中是否含有BUS/SUBWAY/WALK判断
                    all_walk = True
                    has_bus = False
                    for route in trip["routes"]:
                        typ = route["type"]
                        if typ != routing_pb2.JOURNEY_TYPE_WALKING:
                            all_walk = False
                            break
                        if typ == routing_pb2.JOURNEY_TYPE_BY_BUS:
                            has_bus = True
                    if all_walk:
                        non_vehicle_trips += 1
                    elif has_bus:
                        public_transport_trips += 1
                else:
                    # 根据trip中的mode判断
                    if trip["mode"] in [trip_pb2.TRIP_MODE_BUS_SUBWAY_WALK, trip_pb2.TRIP_MODE_BUS_WALK, trip_pb2.TRIP_MODE_SUBWAY_WALK]:
                        public_transport_trips += 1
                    elif trip["mode"] in [trip_pb2.TRIP_MODE_BIKE_WALK, trip_pb2.TRIP_MODE_WALK_ONLY]:
                        non_vehicle_trips += 1
                pos = trip["end"]

    upload_data = [
        {
            "class": "statistics",
            "data": {
                # 总出行次数
                "total_trips": total_trips,
                # 公共交通出行次数
                "public_transport_trips": public_transport_trips,
                # 非机动化出行次数
                "non_vehicle_trips": non_vehicle_trips,
                # 公共交通分担率
                "public_transport_ratio": public_transport_trips / total_trips if total_trips > 0 else 0,
                # 公共交通机动化分担率（仅考虑机动化出行）
                "public_transport_ratio_in_vehicle": public_transport_trips / (total_trips - non_vehicle_trips) if total_trips - non_vehicle_trips > 0 else 0,
            }
        }
    ]
    for t in trips:
        upload_data.append(
            {
                "class": "trip",
                "data": t,
            }
        )

    coll = client[args.output_db][args.output_coll]
    if coll.count_documents({}) > 0:
        print("数据库中已存在数据，请先清空，确认请输入y")
        if input() != "y":
            return
        coll.drop()
        print("数据库已清空")
    # batch insert
    for i in range(0, len(upload_data), 1000):
        coll.insert_many(upload_data[i : i + 1000])
    print(f"插入完成，共{len(upload_data)}条")


if __name__ == "__main__":
    main()
