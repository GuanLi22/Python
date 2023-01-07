f = open("1.jpg",mode="rb")
for i in f:
    print(i)


f = open("bytes_file",mode="wb")
s = '什么都没有'
f.write(s.encode()) #写入utf-8的字符