# -*- coding: utf-8 -*-
# @Time : 2023/1/22 20:26
# @Author : GuanLi
# Written by Pycharm


name1 = "Guan Li"
#* 这是全局变量 有效范围是整个程序
print("修改前",name1)

def change_name():
    name = "666"  #* 这是局部变量, 只在函数范围内生效
    print("这是函数内", name) # 换句话说就是在函数范围内定义的变量就是局部变量只在函数范围内生效
    #! 注变量查找的优先级是 局部>全局
    
    #! 当局部变量和全局变量重名 函数内使用局部变量 其他地方使用全局变量
    
    #! 在函数内声明与全局变量相同名称的变量 不是修改全局变量
    
    # 全局变量可以声明后修改
    global name1 #* 声明一个全局变量(*不建议用)
    name1 = "123"
    


change_name()
print("这是函数外", name1)

