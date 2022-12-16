name = ["alex", "guanli", "alexander", "bell","frank", "poul", "jack", "lucy"]
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


# 正着切
# >>> name[1:3]
# ['jack', 'alexander']
# >>> name[:2]        0可以省略
# ['alex', 'jack']
# >>> name[2:]       后面也可以省略
# ['alexander', 'zhang wei', 'tom']
# >>> name[2:7]      超标写法
# ['alexander', 'zhang wei', 'tom']

# 倒着切
# >>>  name[-4:-1]
# ['jack', 'alexander', 'zhang wei']
# >>> name[-4:]         前后均可省略
# ['jack', 'alexander', 'zhang wei', 'tom']
# >>> name[:-3]
# ['alex', 'jack']


# 步长 name[start:end:step]  step是步长 默认是1

# >>> name[1:8]
# ['guanli', 'alexander', 'bell', 'frank', 'poul', 'jack', 'lucy']

# >>> name[1:8:2]    隔一个一切
# ['guanli', 'bell', 'poul', 'lucy']

# >>> name[1::2]  可以省略
# ['guanli', 'bell', 'poul', 'lucy']

# 2 = 跳一个切一个
# 3 = 跳两个切一个.....

# **前面输入1后切偶数 不输入或输入0切奇数
# eg.
# >>> name[::2]
# ['alex', 'alexander', 'frank', 'jack']

# >>> name[0::2]
# ['alex', 'alexander', 'frank', 'jack']


# 列表的排序
# >>> name = ["alex", "guanli", "alexander", "bell","frank", "poul", "jack", "lucy"]
# >>> name.sort()
# >>> name
# ['alex', 'alexander', 'bell', 'frank', 'guanli', 'jack', 'lucy', 'poul']

# >>> number = [1,34,324,53346,32,5,7,8,3,3,7,8,9,1,3,67,9,786,34,2,4,236,2,7,8,9,3,36,8,546,34]
# >>> number.sort()
# >>> number
# [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 32, 34, 34, 34, 36, 67, 236, 324, 546, 786, 53346]
# 数字 - 英文大写 - 英文小写 - 其他语言


# 例表的反转
# >>> number = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 32, 34, 34, 34, 36, 67, 236, 324, 546, 786, 53346]
# >>> number.reverse()
# >>> number
# [53346, 786, 546, 324, 236, 67, 36, 34, 34, 34, 32, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 5, 4, 3, 3, 3, 3, 2, 2, 1, 1]



#遍历列表的值
# >>> for i in number:
#       print(i)
# 53346
# 786
# 546
# 324
# 236
# 67
# 36
# 34
# ...

# 打印出索引
for i in enumerate(number):
    print(i)
# output:
# (0, 53346)
# (1, 786)
# (2, 546)
# (3, 324)
# (4, 236)
# (5, 67)
# ....

for i in enumerate(number):
    print(i[0],i[1])
# output:
# 0 53346
# 1 786
# 2 546
# 3 324
# 4 236
# 5 67