import random
staff_list = []
for i in range(1, 301):
    staff_list.append(f"员工{i}")
level = [3, 6, 10]
count = 0
for j in range(3):
    winner_list = random.sample(staff_list, level[j])
    data = " ".join(winner_list)
    for user in winner_list:
        staff_list.remove(user)
    print(f"获得{j+1}等奖的是：{data}", end="")
    print()