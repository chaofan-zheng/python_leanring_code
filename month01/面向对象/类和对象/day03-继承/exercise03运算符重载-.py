"""
    练习：运算符重载
    实现自定义类型的减法与乘法运算
"""


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if type(other) == Vector:
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
        else:
            x = self.x + other
            y = self.y + other
            z = self.z + other
        return Vector(x, y, z)

    def __sub__(self, other):
        if type(other) == Vector:
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
        else:
            x = self.x - other
            y = self.y - other
            z = self.z - other
        return Vector(x, y, z)

    def __mul__(self, other):
        if type(other) == Vector:
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
        else:
            x = self.x * other
            y = self.y * other
            z = self.z * other
        return Vector(x, y, z)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"


pos01 = Vector(1, 2, 3)
pos02 = Vector(2, 3, 4)
pos03 = pos01 + pos02
print(pos03)
pos04 = pos01 - pos02
pos05 = pos01 * pos02
