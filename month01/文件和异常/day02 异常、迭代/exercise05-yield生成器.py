"""
    迭代器
"""
class StudentController: # 可迭代对象:返回迭代器
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    def __iter__(self):
        # 生成迭代器代码的大致规则:
        # 1. 将yield关键字以前的代码存储到__next__函数体中
        # 2. 将yield关键字以后的数据作为__next__函数返回值
        index = 0
        yield self.__list_students[index]

        index += 1
        yield self.__list_students[index]

        index += 1
        yield self.__list_students[index]

if __name__ == '__main__':
    controller = StudentController()
    controller.add_student("孙浩")
    controller.add_student("陈小峰")
    controller.add_student("杨旭")
    for item in controller:
        print(item)
    # iterator = controller.__iter__()
    # while True:
    #     try:
    #         item = iterator.__next__()
    #         print(item)  #
    #     except StopIteration:
    #         break