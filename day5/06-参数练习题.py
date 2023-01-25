# -*- coding: utf-8 -*-
# @Time : 2023/1/22 13:17
# @Author : GuanLi
# Written by Pycharm


def print_info(Hobbies="大保健",*args, **kwargs):
    a = "info"
    a = a.center(20,"-")
    print(a)
    print("Name:", kwargs["name"]) #可以用kwargs.get来取值 这样可以防止取不到报错
    print("Age:",kwargs["age"])
    print("Sex:",kwargs["sex"])
    print("Hobbies:", Hobbies)


print_info(name="Alex", age=22, sex="M")
print_info(name="Jack", age=26, sex="M", Hobbie="学习")
