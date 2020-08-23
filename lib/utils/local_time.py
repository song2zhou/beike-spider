# !/usr/bin/env python
# coding=utf-8
# author: sunshinebooming@gmail.com

import time

def get_local_time_string() :
    """
    返回形如"2020-11-11"这样的时间字符串
    """
    current = time.localtime()
    return time.strftime("%Y-%m-%d", current)