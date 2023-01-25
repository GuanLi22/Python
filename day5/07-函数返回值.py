# -*- coding: utf-8 -*-
# @Time : 2023/1/22 13:44
# @Author : GuanLi
# Written by Pycharm


def stu_reg(name, age, course, country="CN"):  # 把country变成默认参数 必须移到最后面
    a = "学生注册信息"
    print(a.center(30, "-"))
    print("name:", name)
    print("age:", age)
    print("country:", country)
    print("course:", course)

    if age > 22 or country == "US":
        return False
    else:
        return True


status = stu_reg("王山炮", 22, course="python全栈开发", country="US")
if status:
    print("成功")
else:
    print("缺少条件")
