"""
    内置高阶函数
"""


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

# map
for item in map(lambda item: item.eid, list_employees):
    print(item)

# filter
for item in filter(lambda item: item.money > 20000, list_employees):
    print(item)
print()
# sorted
for item in sorted(list_employees,key =lambda emp:emp.money):
    print(item)
