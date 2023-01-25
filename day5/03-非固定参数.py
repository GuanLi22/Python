# -*- coding: utf-8 -*-
# @Time : 2023/1/22 12:54
# @Author : GuanLi
# Written by Pycharm

def stu_reg(name, age, *args):  # *args会把多传入的数据变成一个元组
    print(name, age, args[1])
    print(args,type(args))


# stu_reg("guanli", 15)
stu_reg("guanli", 15, 114514, "腾讯")




def stu_reg1(name, age, **kwargs):
    print(name, age, kwargs)
    print(kwargs,type(kwargs))
# 当你输入关键参数（指定参数）时 会以key:value形式存进字典


stu_reg1("guanli", 15, hobby="computer", address="长春")
