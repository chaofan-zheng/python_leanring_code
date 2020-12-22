"""
    架构
        餐厅架构
            迎宾 -- 点餐服务员 -- 厨师 -- 送菜服务员
        软件架构
            视图 View                     控制 Controller
                负责界面逻辑，负责输入输出           业务逻辑（一些核心算法）

                          模型  Model
                                数据抽象
"""


# 学生信息管理系统

"""
    学生信息管理系统
"""


class StudentModel:
    """
        数据模型：封装数据
    """

    def __init__(self, name="", age=0, score=0.0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 学生编号(全球唯一标示符)
        self.sid = sid

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise Exception("成绩有误")


class StudentView:
    """
        界面视图：负责处理界面逻辑(input/print)
    """

    def __init__(self):
        # 对象.实例变量 = 类名()
        self.__controller = StudentController()    # 这里不需要有变化

    def __display_menu(self):
        print("1) 获取学生信息")
        print("2) 显示学生信息")
        print("3) 删除学生信息")
        print("4) 修改学生信息")

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

    def main(self):                     # 给用户一个入口，其他的详细的方法进行封装
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
        stu.sid = input("请输入需要修改的学生编号：")
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = input("请输入需要修改的学生年龄：")
        stu.score = input("请输入需要修改的学生成绩：")
        if self.__controller.modify(stu):
            print("改对喽")
        else:
            print("失败啦")


class StudentController:
    """
        逻辑控制器：负责处理业务逻辑(存储/查询)
    """

    def __init__(self):
        self.__list_students = []
        # 重命名：shift+f6
        self.__start_sid = 1001

    @property   # 只读属性
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

    def modify(self, stu_target):
        for stu in self.__list_students:
            if stu.sid == stu_target.sid:
                # stu = stu_target # 错误:改栈帧变量
                # 正确：改学生信息
                stu.name = stu_target.name
                stu.age = stu_target.age
                stu.score = stu_target.score
                return True
        return False

        # 错误：改列表变量
        # for i in range(len(self.__list_students)):
        #     if self.__list_students[i].sid == stu_target.sid:
        #         self.__list_students[i] = stu_target


# 入口
view = StudentView()
view.main()
