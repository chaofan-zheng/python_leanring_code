class MyClass:
    def __init__(self):
        self.__data = 10

    def __func01(self):
        print("func01 被执行了")


m01 = MyClass()
# print(m01.__data)  # 报错  type object 'MyClass' has no attribute '__data'
print(m01.__dict__)
m01._MyClass__func01()    # 隐形变量的显示方式 但是不建议，是臭流氓做法
print(m01._MyClass__data)
