import pandas
import os
import re

def house_price_info_2_excel() :
    file_list = os.walk("./data")
    for file in file_list :
        print(file)

    return

    """
    subject = r"./data/[a-z]{2,2}/[0-9]{4,4}-[0-9]{1,2}-[0-9]{1,2}/[0-9]{4,4}-[0-9]{1,2}-[0-9]{1,2}.csv"
    file_path = re.findall()
    """
    is_exists = os.path.exists("./data/wh/2020-08-24/2020-08-24.csv")
    if not is_exists :
        print("csv file not exitsts")
        return
    
    csv_file = pandas.read_csv("./data/wh/2020-08-24/2020-08-24.csv", encoding="ansi")

    is_exists = os.path.exists("./data/analysis/wh")
    if not is_exists :
        print("analysis path not exitsts")
        os.makedirs("./data/analysis/wh")

    csv_file.to_excel("./data/analysis/wh/2020-08-24.xlsx", sheet_name = "house_price")

if __name__ == "__main__" :
    house_price_info_2_excel()