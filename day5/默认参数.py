#-*- coding: utf-8 -*-
#@Time : 2023/1/22 12:54
#@Author : GuanLi
# Written by Pycharm


def stu_reg(name, age, course, country="CN"):  # 把country变成默认参数 必须移到最后面
    a = "学生注册信息"
    print(a.center(30,"-"))
    print("name:", name)
    print("age:", age)
    print("country:", country)
    print("course:", course)


stu_reg("王山炮", 22, "python_devops")
stu_reg("张叫春", 21, "linux", country="JP") # 可以修改默认参数country
stu_reg("刘老根", 25, "linux", "US") # 也可以不写参数名
