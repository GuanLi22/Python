a = "guanli liguan guanli 2007"

print(a.center(50, "-"))   #output : ----------------------guanli----------------------
# 使整个长度为50，把字符串居中其他用“”里的字符填充

print(a.count("g")) #output : 3
#查找字符串中某个字符出现次数

print(a.count("g",0,5)) #output : 1
#从0-5之内查找

print(a.endswith("7"))  #output : True
#判断字符串是否以7结尾

print(a.startswith("g"))  #output : True
#判断字符串是否以g开头

print(a.find("n")) #output : 3
#字符查找，没找到返回-1，找到返回字符的索引。从左往右按顺序查找找到后即停止，返回索引

print(a.isdigit()) #output : False
#判断字符串是否为整数

l = ["fu", "ck", "y", "ou"]
print("".join(l)) #output : fuckyou
#将列表拼接（连接）成字符串

print(a.replace("g", "G", 1)) #output : Guanli liGuan Guanli 2007
#替换字符串中字符，后面为替换次数

print(a.split()) #output : ['guanli', 'liguan', 'guanli', '2007']
#将字符串转换为列表，
# print(a.split("l")) 括号内可以添加参数，不添加默认以空格为分割，“”里的值就表示以什么为界限分割， 分割后“”里的值会被删除，
# print(a.split("l", 1)) 后面的1为分割一次