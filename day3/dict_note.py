
#结构 ： {key1:value1,key2:value2}
staff_dic = {
    "Alex":[23,"ceo",100000],
    "guanli":[16,"sb",0],
    "Alexander":[100000,"nb",10000000000000000],
    "Alexander":[100000,"sb",10]
}
print("Alex" in staff_dic)
# 如果重复后面会覆盖前面的值
print(staff_dic["Alexander"])   #output : [100000, 'sb', 10]
print(staff_dic["Alex"][0])   #可以这样取值


# 增加的操作
staff_dic["神仙"] = [9999999999,"znb",999999999999999999999999999]
print(staff_dic)



