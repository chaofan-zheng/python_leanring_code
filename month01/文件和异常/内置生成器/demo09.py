"""
查找最有钱的员工
查找xxx员工
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid},部门编号是{self.did},工资是{self.money}"


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def find_all_name():
    for item in list_employees:
        yield item.name


def find_all_eid_money():
    for item in list_employees:
        yield item.eid, item.money


result01 = IterableHelper.select(list_employees, lambda item: item.name)
result02 = IterableHelper.select(list_employees, lambda item: (item.eid, item.money))
for item in result01:
    print(item)
for item in result02:
    print(item)


