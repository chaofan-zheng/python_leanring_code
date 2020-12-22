class Father:
    def __init__(self, a, b, c):
        self.c = c
        self.b = b
        self.a = a
        print(self.a)
        print(self.b)
        print(self.c)


class Child(Father):
    def __init__(self, child, a, b, c):
        super().__init__(a, b, c)
        self.child = child
        print(self.child)


child = Child(1, 2, 3, 4)
