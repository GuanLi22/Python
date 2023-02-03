# -*- coding: utf-8 -*-
# @Time : 2023/01/25 14:09:13
# @Author : GuanLi
# Written by Visual Studio Code


# abs 取绝对值
print(abs(-10))
print("---------------------")


# all 返回输入的list dict 等可循环文件的true false情况 #*如果为都true返回true, 有一个或多个为false返回false*
# 或者说必须全部为true 才会返回true
a = [1, 2, 3, 4, 5, 6, 7]
print(all(a))
print("---------------------")


# any 只要有一个为true 就返回true
b = [0, 1, 2, 3, 4, 5, None, 0, 0]
print(any(b))
print("---------------------")


# bool返回输入参数的true false状态, python中只有 0 和 None 表示false , 剩下的不管是复数 还是正数 还是true 都返回true
print(bool(0))
print(bool(None))
print(bool(1))
print(bool(-1))
print(bool(True))
print("---------------------")


# chr 打印ASCII值对应的字符
print(chr(90))
print("---------------------")


# ord 打印字符所对应的ASCII值
print(ord("Z"))
print("---------------------")


# dict 生成一个空字典 等字典的用法
print(dict())  # 生成一个空字典
# 当然也可以这样 a = {}
print(dict(name="guanli", age="15"))  # 创建一个字典并把你输入的值以key:value的形式存入字典
print("---------------------")


# list 同dict


# dir 会把当前环境下的所有变量名存到列表中
print(dir())
print("---------------------")


# locals 会把当前环境下的所有变量名以及变量值存到字典中
print(locals())
print("---------------------")


# map 可以把参数中 后面的可循环文件 交给 前面的函数 运算
# 但py3要在循环中才会运行
l = list(range(10))
ll = list(range(9))
def calc(x):  # 可以定义多个参数
    return 2 * x
for i in map(calc, l):
    print(i)

print("lllllllllllllllllllllll")

def calc1(x, y):
    return x + y
for f in map(calc1, l, ll):
    print(f)
print("---------------------")


# filter (function or None, iterable)
# 英文筛选器 作用就是把后面的 可迭代对象 交给前面的 函数 运行
# 如果函数返回的是true就保留数据 返回false或None的值不会接收
for p in filter(lambda x: x % 2 == 1, a):
    print(p)

print("lllllllllllllllllllllll")

def compare(x):
    if x >= 3:
        return x
    else:
        return False
for k in filter(compare, a):
    print(k)
print("---------------------")


# max 求一个可迭代对象的最大值
print(l)
print(max(l))
print("---------------------")


# min 求一个可迭代对象的最小值
print(l)
print(min(l))
print("---------------------")


# sum 将可迭代对象的值求和
print(l)
print(0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)
print(sum(l))
print("---------------------")


# enumerate 多用于在for循环中同时获得索引和值，即需要index和value值的时候可以使用enumerate
name = ["alex", "guanli", "alexander", "bell", "frank", "poul", "jack", "lucy"]
for index, value in enumerate(name):
    print(index, value)
print("---------------------")


# round 用来取小数保留的位数
print(round(3.1415626))  # 默认保留到整数
print(round(3.1415626, 2))  # 后面接参数 表示保留几位小数
print("---------------------")


# type 看类型
print(type("113212"))
print("---------------------")


# zip 几乎同翻译 会把列表里的值一一配对放到一个元组里
# 如果有一边的值超了 就舍弃了
count = [1, 2, 3, 4, 5, 6, 7, 8]
print(zip(name, count))
for i in zip(name, count):
    print(i)
# output:
'''<zip object at 0x000002057083A6C0>
('alex', 1)
('guanli', 2)
('alexander', 3)
('bell', 4)
('frank', 5)
('poul', 6)
('jack', 7)
('lucy', 8)
'''
print("---------------------")

