"""
本文件用于将人的出行拆分为一段一段的Trip（有时候也称为OD）
"""

import argparse
from pymongo import MongoClient
from pycitydata.map import Map


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
                pos = trip["end"]
    coll = client[args.output_db][args.output_coll]
    if coll.count_documents({}) > 0:
        input("数据库中已存在数据，请先清空，确认请输入y")
        if input() != "y":
            return
        coll.drop()
        print("数据库已清空")
    # batch insert
    for i in range(0, len(trips), 1000):
        coll.insert_many(trips[i : i + 1000])
    print(f"插入完成，共{len(trips)}条")


if __name__ == "__main__":
    main()
