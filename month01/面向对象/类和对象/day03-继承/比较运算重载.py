"""
实现自定义类型列表，获取最大和删除功能
"""


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    # def __gt__(self, other):
    #     if self.r + self.g + self.b > other.r + other.g + other.b:
    #         return True

    def __lt__(self, other):
        if self.r + self.g + self.b < other.r + other.g + other.b:
            return True
        # 也可以写小于。但是祖师爷又有大于又有小于的时候就是为了当，大于和小于的逻辑不一样的时候。

    # def __eq__(self, other):
    #     if self.r == other.r and self.g == other.g and self.b == other.b:
    #         return True

    def __str__(self):
        return f"R:{self.r},G:{self.g},B:{self.b}"


list_color = [
    Color(100, 200, 100),
    Color(200, 100, 150),
    Color(90, 20, 0),
]

print(max(list_color))
list_color.remove(Color(90, 20, 0))
for item in list_color:
    print(item)
