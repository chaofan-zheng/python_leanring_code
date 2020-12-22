"""

"""


class A:
    def func01(self):
        print("A - func01")


class B(A):
    def func01(self):
        print("B - func01")
        super().func01()


class C(A):
    def func01(self):
        print("C - func01")
        super().func01()


class D(B,C):
    def func01(self):
        print("D - func01")
        # 缺点:只能调用继承列表第一位
        super().func01()
        # 通过类名 调用 实例方法
        # C.func01(self)

d = D()
d.func01()
