# -*- coding: utf-8 -*-
# @Time : 2023/01/25 12:50:23
# @Author : GuanLi
# Written by Visual Studio Code


d ={"name":"Alex","age":26,"hobbie":"大保健"}
l=["Rebeeca","Katrina","Rachel"]

# 在函数内可以更改 字典或列表 里的值但不能改变 字典或列表 本身
def change_data(info, girls):
    info["hobbie"]="学习"
    girls.append("XiaoYun")
    
change_data(d, l)
print(d, l)