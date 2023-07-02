# -*- coding: utf-8 -*-
# @Time : 2023/2/2 9:47
# @Author : GuanLi
# Written by Pycharm

import random


# 1.确定游戏人数
# 2.确定游戏人的姓名
name_list = []
def card_sending_program():
    player_num = int(input("请输入游戏人数(最多18人)：").strip())
    if 0 > player_num > 18:
        print("人数无效")
        exit()
    for i in range(player_num):
        player_name = input(f"第{i + 1}位玩家姓名").strip()
        name_list.append(player_name)

