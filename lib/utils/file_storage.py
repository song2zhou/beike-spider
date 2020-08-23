# !/usr/bin/env python
# coding=utf-8
# author: sunshinebooming@gmail.com

import os
import inspect
import sys

def get_root_path() :
    # 获取当前脚本路径
    current_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    # 获取工程根目录路径
    uitils_path = os.path.dirname(current_path)
    lib_path = os.path.dirname(uitils_path)
    root_path = os.path.dirname(lib_path)

    return root_path