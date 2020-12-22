"""
小明使用手机打电话
   要求:增加座机,卫星电话时不影响小明.

"""
from typing import Any


class Person:
    def __init__(self, name):
        self.name = name

    def telecommunication(self, tele_facility):
        tele_facility.call()


class TeleFacilities:
    def __init__(self, name):
        self.name = name

    def call(self):
        pass


class MobilePhone(TeleFacilities):
    def __init__(self, name):
        super().__init__(name)

    def call(self):
        print(f"{self.name}正在拨打中")


class Landline(TeleFacilities):
    def __init__(self, name):
        super().__init__(name)

    def call(self):
        print(f"{self.name}正在拨打中")


class Satellite(TeleFacilities):
    def __init__(self, name):
        super().__init__(name)

    def call(self):
        print(f"{self.name}正在拨打中")


xiaoming = Person("小明")
xiaoming.telecommunication(MobilePhone("手机"))
