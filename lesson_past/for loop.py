guanli_name = 14
for i in range(3):
    guessname = int(input('猜猜我几岁:'))
    if guessname > 14:
        print('猜大了')
    elif guessname < 14:
        print('猜小了')
    else:
        print('猜对了')
        exit('6666')
        
#         或者使用exit('猜对了')
print('sb吧你')
