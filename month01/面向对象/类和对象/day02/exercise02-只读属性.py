"""
只读属性
创建桌子类
    数据：品牌，材质，尺寸（长宽高）
"""


class Table:
    def __init__(self):
        self.__brand = input("请输入品牌")
        self.__material = "复合板材"
        self.__size = (2,2,2)

    @property
    def brand(self):
        return self.__brand

    @property
    def material(self):
        return self.__material

    @property
    def size(self):
        return self.__size


yijiazhuozi = Table()
print(yijiazhuozi.size)
# yijiazhuozi.size = (1,1,1) # AttributeError: can't set attribute
