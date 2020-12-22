"""
    让for循环操作自定义对象
"""


class ControllerIterator:
    def __init__(self, list_graphic):
        self.list_graphic = list_graphic
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.list_graphic) - 1:
            raise StopIteration
        return self.list_graphic[self.index].name


class GraphicController:
    def __init__(self, name=""):
        self.name = name
        self.list_graphic = []

    def add_graphic(self, name):
        self.list_graphic.append(GraphicController(name))

    def __iter__(self):
        return ControllerIterator(self.list_graphic)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")
# print(controller.list_graphic)
#
for item in controller:
    print(item)
