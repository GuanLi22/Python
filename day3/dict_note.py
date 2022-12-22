
#结构 ： {key1:value1,key2:value2}

staff_dic = {
    "Alex":[23,"ceo",100000],
    "Guan Li":[16,"sb",0],
    "Alexander":[100000,"nb",10000000000000000],
    "Alexander":[100000,"sb",10]
}
print("Alex" in staff_dic) # output : True
# 如果重复后面会覆盖前面的值
print(staff_dic["Alexander"])   #output : [100000, 'sb', 10]
print(staff_dic["Alex"][0])   #可以这样取值


# 增加的操作
# 就是  字典[新增的key] = 新数据
staff_dic["神仙"] = [9999999999,"znb",999999999999999999999999999]
print(staff_dic)


# 删除的操作
staff_dic.pop("神仙") # 输入指定的key，可以连｛指定key｝和｛它所代表的数据｝一并删除  （直接删）

del staff_dic["神仙"] # 同上pop

# 清空字典
staff_dic.clear() # 清空dict


# 修改字典 (或者说是替换指定key的value值)
# 简单的解释  dict[已有的key] = 你要更换的数据
staff_dic["Guan Li"] = [16,"dsb",0]


# 字典的查询
# 判断值是否在字典里
"Guan Li" in staff_dic #  查key  若在返回True 不在返回False

staff_dic["Alex"]  #返回对应key的值 若不在 则报错

staff_dic.get("Alex", default = None)   #返回对应key的值 若不在返回default的值 默认为 None

staff_dic.keys()   #返回字典中 所有的key

staff_dic.values()  #返回字典中 所有的value

staff_dic.items()  #返回一个包含所有key，value的元组
# output :  dict_items([('Alex', [23, 'ceo', 100000]), ('Guan Li', [16, 'sb', 0]), ('Alexander', [100000, 'sb', 10])])


# 字典的循环
for i in staff_dic.keys():  #有这几种方法
    print(i)

for k,v in staff_dic.items(): #这种方法要现转成列表，效率低
    print(k,v)

for b in staff_dic:  #这种方法效率高
    print(b)
# 如果想取value
    print(b,staff_dic[b])



# 求字典的长度
len(staff_dic)
# 数字没有长度


# 字典嵌套
# 同列表
staff_dic[3] = {5:1000}

# 取用
staff_dic[3][5]



