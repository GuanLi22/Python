# -*- coding: utf-8 -*-
# @Time : 2023/1/10 22:19
# @Author : GuanLi

import re

name = "guanli15Alex16zhangwei30"
# 现在只要名字
name_list = re.split("[1234567890]", name)  # 看见[]内的任意一个值都切 后面切name
