
from mysqlManager import *

def select_menu():
    print('1.添加')
    print('2.显示')
    print('3.删除')
    print('4.修改')
    print('5.排序')
    print('6.退出')
    item = input('请输入选项编号：')
    if item == '1':
        add_stu()
    elif item == '2':
        get_stu()
    elif item == '3':
        del_stu()
    elif item == '4':
        change_stu()
    elif item == '5':
        order_by_score()
    elif item == '6':
        print('感谢您的使用，欢迎再来')
        return False
    else:
        print('输入错误~\n请检查信息')
    return True

def add_stu():
    name = input('请输入学员姓名：')
    score = input('请输入学员成绩：')
    age = input('请输入学员年龄：')
    add_student(name, score, age)

def get_stu():
    students = get_student()
    for item in students:
        print(f"学号：{item['id']} 姓名：{item['name']}  分数：{item['score']} 年龄：{item['age']}")

def del_stu():
    stu_del_id = int(input('请输入你要删除的学员id：'))
    all_id = get_all_id()
    if stu_del_id in all_id:
        delete_student(stu_del_id)

def change_stu():
    change_stu_id = int(input('请输入你要修改的学员的id:'))
    name = input('请输入修改之后的学员姓名：')
    score = input('请输入修改之后的学员成绩：')
    age = input('请输入修改之后的学员年龄：')
    all_id = get_all_id()
    if change_stu_id in all_id:
        change_student(change_stu_id, name, score, age)

def order_by_score():
    student = order_by_score_desc()
    for item in student:
        print(f"学号：{item['id']} 姓名：{item['name']}  分数：{item['score']} 年龄：{item['age']}")

def main():
    while True:
        print('欢迎进入学生管理系统：')
        if not select_menu():
            break

main()
