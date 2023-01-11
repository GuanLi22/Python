# -*- coding: utf-8 -*-
# @Time : 2023/1/7 17:38
# @Author : GuanLi

#文件修改 替换而是往后挤
# 把内容都加载到内存里 再重新写到硬盘
f = open("stock_data", mode="r+", encoding="utf-8")



# 1.加载到内存
data = f.read() # 括号里可以跟参数 输入几个字符 就读几个

# print(data.replace("代码","带吗")) #用字符串的replace替换功能，吧”代码“，替换为“带吗”

new_data = data.replace("代码", "带吗")

# 2.把文件清空
f.seek(0)
f.truncate() #截断文件 后面参数是字符

# 3.写入新内容
f.write(new_data)


# 4.保存并退出
f.close()