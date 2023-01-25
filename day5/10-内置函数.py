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

# dict 生成一个空字典 等字典的用法
print(dict()) # 生成一个空字典
print(dict(name="guanli", age="15")) # 创建一个字典并把你输入的值以key:value的形式存入字典
print("---------------------")
