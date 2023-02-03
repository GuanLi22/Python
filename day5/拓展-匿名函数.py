# -*- coding: utf-8 -*-
# @Time : 2023/1/27 16:30
# @Author : GuanLi
# Written by Pycharm

# 正常使用def定义函数
def clac1(x):
    return x + 1


print(clac1(3))



# 使用匿名函数表达
clac2 = lambda x: x + 1

print(clac2(3))

# 可以结合map filter 等函数一起使用
a = [1, 2, 3, 4]
res = map(lambda x: x+1, a)
print(res)

# py2中会返回列表  [2, 3, 4, 5]
# py3中会返回迭代器  <map object at 0x0000019E28F663E0>
