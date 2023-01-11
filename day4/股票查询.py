# -*- coding: utf-8 -*-
# @Time : 2023/1/10 9:11
# @Author : GuanLi

import re

# 股票查询要求：
# 开发程序对 stock data.txt 进行以下操作:

# 1.程序启动后，给用户提供查询接口，允许用户重复查股票行情信息。
stock_dict = {}

with open("stock_data.txt", mode="r", encoding="utf-8") as f: #打开文件
    headers = f.readline().strip().split(",")


    for line in f:  #遍历文件
        line = line.strip().split(",") #去掉换行，转为列表
        stock_dict[line[0]] = line # 变成dict 将股票代码存为key 整个一行内容存为value




while True:  #允许用户无限的输入信息
    cmd = input("请输入查询指令：").strip()
    for s_key, s_value in stock_dict.items():  # 取出整行内容
        s_name = s_value[1] #把股票名称存起来

# 2.允许用户通过模糊查询股票名，比如输入“啤酒”就把所有名称当中包含啤酒的股票都打印出来。
        if cmd in s_name:
            print(s_value)

# 3.允许按当前价、涨跌幅、换手率这几列来筛选信息，比如输入“当前价>50"则把价格大于50的股票都打印，
#   输入"涨跌幅<50"，则把涨跌幅小于50的股票都打印，不用判断等于。


#这叫做公式查询
# 1.公式的合法性判断 -----正则表达式
    cmd_paser = re.split("[<>]", cmd) #切这个用户输入的指令
    if len(cmd_paser) != 2:  #如果输入的公式不合法,切出来长度就不是2
        print("指令无效")
        continue

# 2.判断列名的合法性
    filter_column, filter_var = cmd_paser
    filter_column = filter_column.strip(" ")
    filter_var = filter_var.strip("%")  #去掉输入时的%
    if filter_column not in ["当前价", "涨跌幅", "换手率"]:
        print("查询对象无效")
        continue


# 3.判断数值的合法性
    try:
        filter_var = float(filter_var)

    except:

        print("查询数值无效")
        continue

# try中运行的代码如果有问题不要报错，运行except中的代码


# 4.处理逻辑
#   1)索引 ------ headers
    column_index = headers.index(filter_column) #返回输入的对象(列名)的索引
    for s_id, s_val in stock_dict.items():
        if ">" in cmd:
            if float(s_val[column_index].strip("%")) > filter_var: #去掉要比对的文件中的%
                print(s_val)
        else:
            if float(s_val[column_index].strip("%")) < filter_var:
                print(s_val)


