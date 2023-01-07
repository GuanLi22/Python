f = open("name_file", mode="r", encoding="utf-8")


for line in f: # 每循环一次 就是读一行
    line = line.split() #详见str_note
    height = int(line[2])
    weight = int(line[3])
    if height >= 170 and weight <= 50:
        print(line)


# 自己写的 麻烦
# final_line = []
# name_list = []
# end_list = []
# for line in f: # 每循环一次 就是读一行
#     line = line.split()
#     final_line.append(line)
# for i in final_line:
#     if int(i[2]) > 170:
#         name_list.append(i)
# for v in name_list:
#     if int(v[3]) < 50:
#         end_list.append(v)
# print(end_list)
#




# print(f.readlines())  # 会把文件变成一个大列表






