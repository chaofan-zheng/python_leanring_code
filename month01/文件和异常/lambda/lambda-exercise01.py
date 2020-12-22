"""
需求：使用lambda改写exercise04
定义函数，在员工列表中查找编号是 1003 的员工
定义函数，在员工列表中查找姓名是孙悟空的员工

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


def find_eid(item):
    return item.eid == 1003


def find_name(item):
    return item.name == "孙悟空"


result_eid = IterableHelper.find_single(list_employees, lambda item: item.eid ==1003)
print(result_eid.__dict__)
result_name = IterableHelper.find_single(list_employees, lambda item: item.name == "孙悟空")
print(result_name.__dict__)