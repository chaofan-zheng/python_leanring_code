"""画出下列代码内存图
   找出打印结果"""
g01 = 100
g02 = 100


def func01():
    g01 = 200


def func02():
    global g02
    g02 = 200


func01()
print(g01)  # 100
func02()
print(g02)  # 200


class MyClass:
    cls01 = 300

    def __init__(self):
        self.ins01 = 400
        self.ins01 += 1
        MyClass.cls01 += 1


instance01 = MyClass()
print(instance01.ins01)  # 401
print(MyClass.cls01)  # ?301

instance02 = MyClass()
print(instance02.ins01)  # ?401
print(MyClass.cls01)  # ?302
