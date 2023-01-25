#-*- coding: utf-8 -*-
#@Time : 2023/1/22 12:55
#@Author : GuanLi
# Written by Pycharm


def stu_rege(name, age, course= "PY", country = "CN"):
    a = "学生注册信息"
    print(a.center(30,"-"))
    print("name:", name)
    print("age:", age)
    print("country:", country)
    print("course:", course)


stu_rege("guanli", course="linux", age=16, country="JP") # 其中guanli为位置参数，其他为指定参数
# 可以这样指定参数， 可以不对应位置
# *注关键参数（指定参数）必须放在位置参数后
