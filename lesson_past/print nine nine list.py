for i in range(1, 10):     #先写一个大循环
    for j in range(1, i+1):     #然后写于个小循环
        print(f"{i}*{j}={i*j}", end=" ")    #end表示以什么结尾这里是空格，正常是/n换行
    print("")

