class Vector:
    def __init__(self, x, y ):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) == Vector:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector(x, y)

    def __iadd__(self, other):
        if type(other) == Vector:
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

pos01 = Vector(2,2)
print(id(pos01))
pos02 = Vector(22,88)

pos03 = pos01+pos02
pos01 += pos02
print(id(pos01))


def __itruediv__(self, other):
    if type(other) == Vector:
        self.x /= other.x
        self.y /= other.y
    else:
        self.x /= other
        self.y /= other
    return self
