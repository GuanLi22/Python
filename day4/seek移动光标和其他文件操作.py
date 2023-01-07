# read
# f = open("helloworld",mode="r",encoding="utf-8")
#
# f.seek(12) #光标移动是靠字节判断的，ASCII每个字符1个字节；utf-8中英文字符和数字1个字节，
#             中文3个字节，\n换行符占两个（不同系统不一样）
# print(f.read())



# write
f = open("helloworld1", mode="w", encoding="utf-8")

f.write("helloworld\n")


print("光标当前位置:", f.tell())  # 返回光标位置


f.write("yeeeeeeeeee\n")  # \n占两个bytes


print("光标当前位置:", f.tell())  # 返回光标位置


# output : helloworld
#          yeeeeeeeeee

f.seek(10)  # 按字节移动，移动光标到第10个bytes


print("光标当前位置:", f.tell())  # 返回光标位置


f.write("------")  # 移动光标后，写字会覆盖

# output : helloworld啥啊eeeeeee






# 其他文件操作
print(f.seekable()) #判断是否可以进行seek操作

print(f.mode) #返回文件的打开模式

f.flush() #把缓存区的数据强制刷新到硬盘

print(f.name)  # 返回文件名

print(f.readable()) #判断文件是否可读

print(f.writable()) #判断文件是否可写

print(f.readline()) #只读一行，遇到 /n 或 /r停止

#没学到的

f.fileno() #返回文件句柄在内核中的索引值，以后做IO多路复用时可以用到

f.truncate() #按指定长度截断文件
#            *指定长度的话，就从文件开头开始截断指定长度，不指定长度的话，就从当前位置到文件尾部的内容全去掉。
