# -*- coding: utf-8 -*-
# @Time : 2023/1/7 21:36
# @Author : GuanLi

import sys

data = sys.argv

old_str = data[1]
new_str = data[2]
file_name = data[3]

# 1.先打开文件
f = open(file_name, mode="r+", encoding="utf-8")

# 2.把文件存储到内存中

data_str = f.read()

# 3.查找要替换的字符出现次数
times_str = data_str.count(old_str)

# 4.修改文件
final_data = data_str.replace(old_str, new_str)

# 5.删除文件
f.seek(0)
f.truncate()

# 6.重新写入文件
f.write(final_data)

# 7.保存并退出
f.close()
print(f"已成功将{old_str}替换为{new_str},一共替换了{times_str}次")









