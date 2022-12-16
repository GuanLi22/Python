name = ["alex", "guanli", "alexander", "bell"]
name2 = ["frank", "poul", "jack", "lucy"]
number = [1, 2, 3]





#列表增加元素
name.append("张伟")#列表后追加元素
name.insert(2,"hhh")#列表中插入元素，这里是列表索引为2的位置插入“hhh”

name.extend(name2)#将两个列表合并

name.insert(2,number)#列表的嵌套

#实例

# >>> name = ["alex","guanli","bell"]
# >>> number = [1,2,3]

# >>> name.insert(1,number)
# >>> name
# ['alex', [1, 2, 3], 'guanli', 'bell']

# 取用
# >>> name[1][2]
# >>> 3

# 更改嵌套进去的列表中的值
# >>> name[1][2] = 4
# >>> name
# >>> ['alex', [1, 2, 4], 'guanli', 'bell']





#列表删除元素
del name [2] #输入索引直接删（解释器自带）

name.pop()#默认删除最后一个值，然后返回删除的值(指定索引)
#可以指定删除对象 name.pop(2)删除第三个 ；name.pop(-2)删除倒数第二个

name.remove("alex")#必须指定元素名称，直接删除，如果有重复的从左到右删





#清空列表

name.clear()





#修改列表
name[1] = 1
# 将索引为二的元素改为1（也可以输入从右往左的索引）





#查询列表

#修改元素的流程
# 先判断
if "alex" in name:
    print("true")
else:
    print("false")
#再查索引
name.index("guanli")
#再修改

name.index("guanli")#返回从右往左匹配到的第一个alex的索引 没找到会报错

name.count("guanli")#返回找到的guanli的个数，没找到不会报错，返回0





# 列表的切片 name[start : end] 注意：左含右不含
name = ["alex","jack","alexander","zhang wei","tom"]
# >>> name[1:3]
# >>> ['jack', 'alexander']
# >>> name[:2]        0可以省略
# >>> ['alex', 'jack']
#



