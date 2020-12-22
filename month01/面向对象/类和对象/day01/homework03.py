"""
创建电脑类,保护数据在有效范围内
        数据:型号,   CPU型号,    内存大小,    硬盘大小
                不超过10个字符    大于0    元组长度大于1
    class Computer:
        def __init__(self, model_number="", cpu="", memory=0, hard_disk=()):
            self.model_number = model_number
            self.cpu = cpu
            self.memory = memory
            self.hard_disk = hard_disk

    alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
    print(alienware.model_number)
    print(alienware.cpu)
    print(alienware.memory)
    print(alienware.hard_disk)
"""


class Computer:
    def __init__(self, model="", cpu="", memory=0, rigid_disk=()):
        self.cpu = cpu
        self.memory = memory
        self.rigid_disk = rigid_disk
        self.model = model

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if 0 <= len(value) <= 10:
            self.__cpu = value
        else:
            raise Exception("cpu型号不能超过10个字符")

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        if 0 <= value:
            self.__memory = value
        else:
            raise Exception("内存必须大于零")

    @property
    def rigid_disk(self):
        return self.__rigid_disk

    @rigid_disk.setter
    def rigid_disk(self, value):
        if len(value) > 1:
            self.__rigid_disk = value
        else:
            raise Exception("硬盘必须要有两个，固态和机械")


alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
apple = Computer("Mackbook pro", "M1", 8, (256,1024))
print(alienware.model)
print(alienware.cpu)
print(alienware.memory)
print(alienware.rigid_disk)
