"""
        定义函数，在员工列表中查找所有薪资大于20000的员工数量
        定义函数，在员工列表中查找所有部门编号是9001的员工数量
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_count(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
"""
from homework.common_homework.iterable_tools import IterableHelper


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


def find_salary_bigger_20000():
    count = 0
    for item in list_employees:
        if item.money > 20000:
            count += 1
            return count


def find_did_9001():
    count = 0
    for item in list_employees:
        if item.did == 9001:
            count += 1
            return count


def condition01(employee):
    return employee.money > 20000


def condition02(employee):
    return employee.did == 9001


result01 = IterableHelper.get_count(list_employees, lambda item: item.money > 20000)
print(result01)
result02 = IterableHelper.get_count(list_employees, lambda item: item.did == 9001)
print(result02)

result03 = IterableHelper.get_min(list_employees,lambda  item: item.eid)
print(result03)
result04 = IterableHelper.get_min(list_employees,lambda item:item.money)
print(result04)

result05 = IterableHelper.order_by(list_employees,lambda item : item.money)
for item in result05:
    print(item.__dict__)

print()
result05 = IterableHelper.order_by(list_employees,lambda item : item.eid)
for item in result05:
    print(item.__dict__)