import pandas
import os
import re

from lib.utils.file_storage import *

def house_price_info_2_excel() :
    csv_path_list = list()

    # 获取工程根目录
    root_path = get_root_path()

    file_pattern = r".*.csv"
    # 遍历查找original_data文件夹下的csv文件
    path_list = os.walk(root_path + "/data/original_data")
    for root,subdir,_file in path_list :
        for __file in _file :
            search_result = re.search(file_pattern, __file)
            if search_result :
                csv_path = os.path.join(root, __file)
                csv_path_list.append(csv_path)

    # 使用pandas将csv文件转换为excel文件，并保存到analysis目录下
    for csv_path in csv_path_list :
        csv_file = pandas.read_csv(csv_path, encoding="utf-8")
        excel_path = csv_path.replace("original_data", "analysis_data")
        excel_path = excel_path.replace("csv", "xlsx")

        # 判断对应城市的目录是否存在，如果不存在则新建
        excel_dir = os.path.dirname(excel_path)
        is_dir_exit = os.path.exists(excel_dir)
        if not is_dir_exit :
            os.makedirs(excel_dir)

        print("saving excel file to", excel_path, "...")
        csv_file.to_excel(excel_path)

if __name__ == "__main__" :
    house_price_info_2_excel()
