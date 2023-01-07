# -*- coding:utf-8 -*-
f = open("name_file.txt", mode="r+", encoding="utf-8")
print(f.readline())
print(f.tell()) # 当前位置39
f.seek(f.tell()) #这个模式有两个光标,直接tell会返回read光标，要seek一下才能写到指定位置
f.write("没了")
