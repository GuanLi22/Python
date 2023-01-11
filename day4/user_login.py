# -*- coding: utf-8 -*-
# @Time : 2023/1/8 21:47
# @Author : GuanLi

# 1.确定用户信息存储在文件里的结构

# 2.把数据读到内存中

accounts = {}

with open("account_data.db", mode="r") as f:
    for line in f:
        line = line.strip().split(",")  # strip 移除字符串首尾指定的字符串；当没有参数时，默认为空格和换行符
        # 把文件先去掉换行符，然后以,分割成列表
        accounts[line[0]] = line
        # 把文件变成字典 并且把用户名变为key 整个一行数据以列表的形式存为value

# 3.循环，让用户输入账号信息，判断

while True:
    username = input("username:").strip()
    if username not in accounts:  # 没有该用户
        print("unknown username,please try again")
        continue

    else:
        if accounts[username][2] == "1":
            exit("你小子被锁了")

    for i in range(3):
        password = input("password:").strip()
        # 去判断密码是否输对了
        if accounts[username][1] == password:
            exit("correct username and password,you are already logined in")
        else:
            print("false password,please try again")
            if i == 1:
                print("\ndo you want to exit? if you want enter 'exit',if not enter 'no'")
                reply = input("")
                if reply == "exit":
                    exit("bye")
        if i == 2:
            print(f"输错{i+1}次密码,{username}你小子被我锁了")
            #第一步先改内存中的dict 再把dict转成原文件格式
            accounts[username][2] = "1"
            with open("account_data.db", mode="w") as f2:
                for user, value in accounts.items():
                    # 把dict转成list
                    lines = ",".join(value) + "\n"
                    # 把list转为str
                    f2.write(lines)
            exit("bye")