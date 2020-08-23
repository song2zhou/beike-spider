# !/usr/bin/env python
# coding=utf-8
# author: sunshinebooming@gmail.com

import re
import os
import requests
import math
import random
import time
from bs4 import BeautifulSoup
from config import *

from lib.utils.local_time import *
from lib.utils.file_storage import *
from lib.request.web_request_header import *

class beike_spider() :
    def __init__(self) :
        pass

    def format_price_info(self, name, price, total) :
        return "{0}, {1}, {2}, {3}\n".format(get_local_time_string(), name, price, total)
    
    def get_price_info(self, city_name) :
        self.city_name = city_name
        self.price_info_list = list()

        target_web = 'http://{0}.fang.ke.com/loupan/'.format(city_name)
        print('request target web:', target_web)
        
        # 获得请求头部
        headers = create_request_headers()
        
        # 发起网页请求（获取总页数）
        response = requests.get(target_web, timeout=10, headers=headers)
        html = response.content
        soup = BeautifulSoup(html, 'lxml')

        # 获得response总页数
        try:
            page_box = soup.find_all('div', class_='page-box')[0]
            matches = re.search(r'.*data-total-count="(\d+)".*', str(page_box))
            total_page = int(math.ceil(int(matches.group(1)) / 10))
        except Exception as e:
            print("warning: only find one page for {0}".format(city_name))
            print(e)

        print('total pages:', total_page)
        headers = create_request_headers()
        # 遍历房价网页
        # for i in range(1, total_page + 1) :
        for i in range(1, 2) :
            target_sub_web = target_web + "pg{0}".format(i)
            print('request target web:', target_sub_web)

            if True == RANDOM_DELAY :
                # 随机延时（0-15）秒
                random_delay = random.randint(0, DELAY_MAX + 1)
                print('random delay: %s S...' %(random_delay))
                time.sleep(random_delay)

            # 发起网页请求
            response = requests.get(target_sub_web, timeout=10, headers=headers)
            html = response.content
            soup = BeautifulSoup(html, 'lxml')

            # 获取房价相关内容
            house_contents = soup.find_all("li", class_ = "resblock-list")
            for house_content in house_contents :
                # 获取单价
                house_price = house_content.find("span", class_ = "number")
                # 获取总价
                house_total = house_content.find("div", class_ = "second")
                # 获取小区名称
                house_name = house_content.find("a", class_ = "name")

                # 整理单价数据
                try :
                    price = house_price.text.strip()
                except Exception as e :
                    price = "0"

                # 整理小区名称数据
                name = house_name.text.replace("\n", " ")

                # 整理总价数据
                try :
                    total = house_total.text.strip().replace(u"总价", " ")
                    total = total.replace(u"/套起", " ")
                except Exception as e :
                    total = "0"

                # 打印单条房价信息
                print("\t===> name: %s, price: %s 元/平米, total: %s" %(name, price, total))

                # 格式化单条房价信息，并添加到list中
                price_fmt_str = self.format_price_info(name, price, total)
                self.price_info_list.append(price_fmt_str)
    
    def store_price_info(self) :
        # 创建数据存储目录
        root_path = get_root_path()
        store_dir_path = root_path + "/data/{0}/{1}".format(self.city_name, get_local_time_string())
        is_dir_exit = os.path.exists(store_dir_path)
        if not is_dir_exit :
            os.makedirs(store_dir_path)
        
        # 存储格式化的房价数据到相应日期的文件中
        store_path = store_dir_path + "/{0}.csv".format(get_local_time_string())
        with open(store_path, "w") as fd :
            for price in self.price_info_list :
                fd.write(price)

if __name__ == "__main__" :
    pass