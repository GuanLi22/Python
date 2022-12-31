f = open("helloworld",mode="r")
# mode 可省略 f = open("helloworld","r")
# r 也可省略 f = open("helloworld")

print(f.read()) # 读出所有内容
print("-----------------------------------")
print(f.readline()) # 读一行
 #  output : helloworld
#            yeeeeeeeeee
#            -----------------------------------
#             （这行没东西）
