# !/usr/bin/env python
# coding=utf-8
# author: sunshinebooming@gmail.com

from lib.request.web_request import *

if __name__ == "__main__" :
    # 创建贝壳网爬虫实例
    spider = beike_spider()
    # 获取网页房价数据
    spider.get_price_info("wh")
    # 存储房价数据
    spider.store_price_info()
