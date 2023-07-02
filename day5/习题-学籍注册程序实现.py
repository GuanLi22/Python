# -*- coding: utf-8 -*-
# @Time : 2023/1/29 15:44
# @Author : GuanLi
# Written by Pycharm

# 自己写的

les_l = ["Python", "Linux", "网络安全", "数据分析", "前端"]
# [guanli,15,13596876997,220724207890213235,python]
data = input("(*注使用,分隔 并且Python和Linux为大写)需要输入姓名,年龄,手机号,身份证号,报名的课程:")
data_list = data.split(",")


def lesson_reg(info):
    if data_list[4] not in les_l:
        print("输入课程名无效,只有Python, Linux, 网络安全, 数据分析, 前端这几个选项")
        exit()
    with open("data.db", "r") as file:
        for line in file:
            res = line.strip("\n").split(",")
            if data_list[2] == res[2] or data_list[3] == res[3]:
                print("身份证或手机号重复,每人只能注册一次")
                exit()
    d = ",".join(info)
    with open("data.db", "a") as f:
        f.write(d)
        f.write("\n")
    print("注册成功")


lesson_reg(data_list)

# q: 这段代码有什么问题?
# a: 1. 课程名输入错误时,会注册成功
#    2. 重复注册时,会注册成功