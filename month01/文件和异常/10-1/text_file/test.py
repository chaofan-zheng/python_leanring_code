class MyClass:
    data02 = 1

    def __init__(self):
        self.data01 = 1
        self.data01 += 1
        MyClass.data02 += 1


m01 = MyClass()
m02 = MyClass()
m03 = MyClass()
print(m03.data01)
print(MyClass.data02)

