# -*- coding: utf-8 -*-
# @Time : 2023/2/2 9:47
# @Author : GuanLi
# Written by Pycharm

db_name = "student_data.db"


def data_processing():
    '''
    数据处理函数
    :return:
    '''
    stu_data = {} #初始化一个空字典
    print("欢迎来到xxxx学城")
    print("请完成学籍注册")

    name = input("姓名:").strip()

    age = input("年龄:").strip()

    phone = input("手机号:").strip()
    #判断输入的手机号是否合法
    if len(phone) != 11 or not phone.isdigit():
        print("输入的手机号不合法")
        exit()

    id_card = input("身份证号:").strip()
    #判断输入的身份证号是否合法
    if len(id_card) != 18:
        print("输入的身份证号不合法")
        exit()

    course_list = ["Python", "Linux", "网络安全", "数据分析", "前端"]
    for index, course in enumerate(course_list):
        print(f"{index + 1}.{course}")

    selected_course = input("请选择课程编号:").strip()
    # 1. 判断输入的课程编号是否合法
    if selected_course.isdigit():
        selected_course = int(selected_course) - 1
        if selected_course < 0 or selected_course >= len(course_list):
            print("输入的课程编号不存在")
            exit()
        else:
            course = course_list[selected_course]
    else:
        print("输入的课程编号不是数字")
        exit()

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["id_card"] = id_card
    stu_data["course"] = course

    return stu_data


#数据核查
def data_check(stu_data):
    '''
    数据核查
    :param stu_data:学员信息dict
    :return:
    '''
    #输入的手机号和身份证号和数据库中已经注册的不能重复
    with open(db_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            _, _, phone, id_card, course = line.split(",")
            if stu_data["phone"] == phone:
                print("输入的手机号已经被注册")
                exit()
            if stu_data["id_card"] == id_card:
                print("输入的身份证号已经被注册")
                exit()

def data_save(db_name, stu_data):  #数据保存
    '''
    把学生数据保存到文件中
    :param db_name:数据库文件名
    :param stu_data:学员信息dict
    :return:
    '''
    with open(db_name, "a", encoding="utf-8") as f:
        f.write(f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_card']},{stu_data['course']}\n")
    print("学籍注册成功")


def main():
    '''
    主函数
    :return:
    '''
    res = data_processing()
    data_save(db_name, res)


main()

#Q:这段代码有错误吗
#A:有，如果输入的姓名是数字，会报错
#Q:如何解决
#A:在输入姓名的时候，判断输入的是否是数字，如果是数字，就报错



