
"""
    方法一
    适合面向过程，适合人工智能方式去做

"""
import exercise

exercise.func01()
my_class = exercise.MyClass()
my_class.func02()
exercise.MyClass.func03()     # 调用类方法，用类名去点类方法



"""
    方法二
    适合面向对象，
"""
from exercise import MyClass, func01

func01()
my_class = MyClass()
my_class.func02()
MyClass.func03()

"""方法三"""
from exercise import *

func01()
my_class = MyClass()
my_class.func02()
MyClass.func03()