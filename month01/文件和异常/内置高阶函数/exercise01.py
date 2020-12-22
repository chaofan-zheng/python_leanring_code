"""
    1. 在商品列表，获取所有名称与单价
    2. 在商品列表中，获取所有单价小于10000的商品
    3. 对商品列表，根据单价进行降序排列
    4. ([1,1],[2,2,2],[3,3,3])
       获取元组中长度最大的列表
"""
from common.iterable_tools import IterableHelper


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

name_and_price = map(lambda item: (item.name, item.price), list_commodity_infos)
for item in name_and_price:
    print(item)
    print()
price_less_than_10000 = filter(lambda item: item.price < 10000, list_commodity_infos)
for item in price_less_than_10000:
    print(item.__dict__)
    print()
price_sorted = sorted(list_commodity_infos, key=lambda item: item.price, reverse=True)
for item in price_sorted:
    print(item.__dict__)

tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])

longest_list = IterableHelper.get_multiple_max(tuple01, lambda item: len(item))
for item in longest_list:
    print(item)
