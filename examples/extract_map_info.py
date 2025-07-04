"""
本文件是利用pycitydata中地图中提取信息并存入MongoDB的示例
"""

import argparse

from pymongo import MongoClient

from pycitydata.map import Map


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mongo_uri", type=str, required=True)
    parser.add_argument("--map_db", type=str, required=True)
    parser.add_argument("--map_coll", type=str, required=True)

    parser.add_argument("--output_db", type=str, required=True)
    parser.add_argument("--out_coll", type=str, required=True)

    return parser.parse_args()


def main():
    args = get_args()
    m = Map(
        mongo_uri=args.mongo_uri,
        mongo_db=args.map_db,
        mongo_coll=args.map_coll,
    )
    print("完成地图信息加载")

    # 道路信息，包含
    # 1. 道路ID
    # 2. 道路名称（如有）
    # 3. 道路长度
    # 4. 道路行车道数
    # 5. 道路起点坐标（lng, lat）
    # 6. 道路终点坐标（lng, lat）
    # 7. 道路最大车速
    total_road_length = 0
    total_driving_lane_length = 0
    road_infos = []
    for road_id, road in m.roads.items():
        length = road["length"]
        road_infos.append(
            {
                "id": road_id,
                "name": road["name"],
                "length": length,
                "lane_count": len(road["lane_ids"]),
                "max_speed": road["max_speed"],
                "start_lnglat": road["shapely_lnglat"].coords[0],
                "end_lnglat": road["shapely_lnglat"].coords[-1],
            }
        )
        total_road_length += length
        total_driving_lane_length += length * len(road["driving_lane_ids"])
    print(
        f"道路信息加载完成，共{len(road_infos)}条，总长度{total_road_length}，总行驶车道长度{total_driving_lane_length}"
    )

    # 信号灯组信息，包含
    # 1. 信号灯组ID（junction_id）
    # 2. 相位数量（fixed_program.phases）
    # 3. 路口坐标
    traffic_light_infos = []
    for junction_id, junction in m.juncs.items():
        if "fixed_program" not in junction:
            continue
        program = junction["fixed_program"]
        if "phases" not in program or len(program["phases"]) == 0:
            continue
        traffic_light_infos.append(
            {
                "id": junction_id,
                "phase_count": len(program["phases"]),
                "lnglat": junction["center_lnglat"],
            }
        )
    print(f"信号灯组信息加载完成，共{len(traffic_light_infos)}条")

    upload_data = []
    for info in road_infos:
        upload_data.append(
            {
                "class": "road",
                "data": info,
            }
        )
    for info in traffic_light_infos:
        upload_data.append(
            {
                "class": "traffic_light",
                "data": info,
            }
        )
    print(f"上传数据准备完成，共{len(upload_data)}条")
    # 上传到MongoDB
    client = MongoClient(args.mongo_uri)
    db = client[args.output_db]
    coll = db[args.out_coll]
    # 检查是否存在
    if coll.count_documents({}) > 0:
        print("数据库中已存在数据，请先清空，确认请输入y")
        if input() != "y":
            print("请重新运行程序")
            return
        coll.drop()
        print("数据库已清空")
    # Batch insert
    for i in range(0, len(upload_data), 1000):
        db[args.out_coll].insert_many(upload_data[i : i + 1000], ordered=False)
    print("上传完成")


if __name__ == "__main__":
    main()
