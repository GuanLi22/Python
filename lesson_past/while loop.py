# # dead loop
# count = 0
# while True:  # 条件永远为真
#     print(f"第{count}次循环....")
#     count += 1
#
# 循环
# count = 0
# while count < 10:
#     print(f'第{count}次循环')
#     count -= 1


guanli_name = 15
yes = 1
no = 0
count = 0
while count < 3:
    guess_name = int(input("猜猜我几岁："))
    if guess_name > 15:
        print("大了")
        count += 1
    elif guess_name < 15:
        print("小了")
        count += 1
    else:
        exit("6")
    if count == 3:
        res = input("你咋这么笨呢还想继续吗？")
        if res == 1:
            count = 0
        elif res == 0:
            exit("好吧")


#
# black_gf_age = 25
# count = 0
# while True:
#     count += 1
#     if count <= 3:
#         guess = int(input("猜猜⿊姑娘多⼤了>>:"))
#         if guess > black_gf_age:
#             print("猜的太⼤了，往⼩⾥试试...")
#         elif guess < black_gf_age:
#             print("猜的太⼩了，往⼤⾥试试...")
#         else:
#             exit("恭喜你，猜对了...")  # 退出程序
#     else:
#         choice = input("猜了3次还不对，真是笨呀，还玩么? [y/Y or n/N]").strip()
#         if len(choice) == 0 : continue # 不能写空值
#         if choice in ("y","Y"):
#             count = 0
#         elif choice in ("n","N"):
#             exit("bye.")
#         else:
#             print("请输⼊正确的选项...")
#
#







