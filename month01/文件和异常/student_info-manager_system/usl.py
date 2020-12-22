"""
    View
"""
from bll import *
from model import *


class StudentView:
    """
        界面视图：负责处理界面逻辑(input/print)
    """

    def __init__(self):
        # 对象.实例变量 = 类名()
        self.__controller = StudentController()

    def __display_menu(self):
        print("输入1增添学生")
        print("输入2显示学生")
        print("输入3删除学生")
        print("输入4更新学生")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            # 对象.实例方法()
            self.__input_student()
        elif item == "2":
            self.__show_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__update_student()

    def __input_student(self):
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        stu = StudentModel(name, age, score)
        # 对象.实例变量.实例方法(参数)
        self.__controller.add_student(stu)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_students(self):
        for stu in self.__controller.list_students:
            print(stu.__dict__)

    def __delete_student(self):
        sid = int(input("请输入学生编号："))
        if self.__controller.remove_student(sid):
            print("啊，删啦")
        else:
            print("哦，失败啦")

    def __update_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = int(input("请输入需要修改的学生年龄："))
        stu.score = int(input("请输入需要修改的学生成绩："))
        if self.__controller.modify(stu):
            print("改对喽")
        else:
            print("失败啦")
