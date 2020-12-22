"""
    业务逻辑层
"""
from common.iterable_tools import IterableHelper
from dal import HouseDao

from model import HouseModel


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
        self.model = HouseModel()

    @property
    def list_houses(self):
        return self.__list_houses

    def show_all_info(self):
        for item in self.__list_houses:
            print(item.__dict__)

    def show_highest_price_info(self):
        result = IterableHelper.get_multiple_max(self.__list_houses, lambda x: x.total_price)
        for item in result:
            print(item.__dict__)

    def show_smallest_area_info(self):
        result = IterableHelper.get_multiple_min(self.__list_houses, lambda x: x.area)
        for item in result:
            print(item.__dict__)

    def ascending_by_total_price(self):
        result = IterableHelper.order_by(self.__list_houses, lambda x: x.total_price)
        for item in result:
            print(item.__dict__)

    def descending_by_area(self):
        result = sorted(self.__list_houses, key=lambda x: x.area, reverse=True)
        for item in result:
            print(item.__dict__)

    def show_all_house_type_info(self):
        result = IterableHelper.get_all_info_count_of_one_item(self.__list_houses, lambda x: x.house_type)
        print(result)


# class Test:
#     def __init__(self, name):
#         self.name = name
#
#
# list01 = [
#     Test("a"),
#     Test("b"),
#     Test("a"),
# ]
#
# print(IterableHelper.get_all_info_count_of_one_item(list01, lambda x: x.name))
