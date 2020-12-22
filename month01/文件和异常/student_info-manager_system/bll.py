"""
    Controller
"""

from model import *


class StudentController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.__list_students = []
        # 重命名：shift+f6
        self.__start_sid = 1001

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu_target):
        # 设置学生的编号(自增长)
        stu_target.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_students.append(stu_target)

    def remove_student(self, sid):
        """
            移除学生
        :param sid:int类型的学生编号
        :return:是否移除成功
        """
        for stu in self.__list_students:
            if stu.sid == sid:
                self.__list_students.remove(stu)
                return True  # 删除成功

        return False  # 删除失败

        # 也可以通过重写 __eq__的函数，来用remove的函数，来移除学生。
        # remove 函数的特点在于如果item不在list里面，会报错，所以要在前面判断在不在里面。

    def modify(self, stu_target):
        for stu in self.__list_students:
            if stu.sid == stu_target.sid:
                # stu = stu_target # 错误:改栈帧变量
                # 正确：改学生信息
                stu.name = stu_target.name
                stu.age = stu_target.age
                stu.score = stu_target.score
                # 也可以写成 stu.__dict__ = stu_target.__dict__
                # 更快捷，更方便
                return True
        return False


if __name__ == '__main__':
    # 测试的时候这么写，正常从main跑的时候不会影响到main的运行
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    for student in controller.list_students:
        print(student)
