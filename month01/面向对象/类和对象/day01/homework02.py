"""
使用封装数据的思想
   创建员工类/部门类,修改实现下列功能.
    1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
    4. 定义函数,查找薪资最少的员工
    5. 定义函数,根据薪资对员工列表升序排列

    # 员工列表
    list_employees = [
        {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
        {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
        {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
        {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
        {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
    ]

    # 部门列表
    list_departments = [
        {"did": 9001, "title": "教学部"},
        {"did": 9002, "title": "销售部"},
    ]
"""


class Employees:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def print_all_info(self):
        print(f"{self.name}的员工编号是{self.eid},部门编号是{self.did},月薪{self.money}元.")

    def print_salary_more_than_2w(self):
        if self.money > 20000:
            self.print_all_info()


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title


# 员工列表
list_employees = [
    Employees(1001, 9002, "师父", 60000),
    Employees(1002, 9001, "孙悟空", 50000),
    Employees(1003, 9002, "猪八戒", 20000),
    Employees(1004, 9001, "沙僧", 30000),
    Employees(1005, 9001, "小白龙", 15000),
]

# 部门列表
list_departments = [
    Department(9001, "教学部"),
    Department(9002, "销售部"),
]


def print_all_employees_department():
    for employee in list_employees:
        for department in list_departments:
            if department.did == employee.did:
                title = department.title
                print(f"{employee.name}的部门是{title},月薪{employee.money}元.")


def find_least_salary():
    min_salary = list_employees[0].money
    employee_name = list_employees[0].name
    for employee in list_employees:
        if employee.money < min_salary:
            min_salary = employee.money
            employee_name = employee.name
    return employee_name


def descending_salary():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].money > list_employees[c].money:
                list_employees[r].money, list_employees[c].money = list_employees[c].money, list_employees[r].money


for employee in list_employees:
    employee.print_all_info()
for employee in list_employees:
    employee.print_salary_more_than_2w()

print_all_employees_department()
print(find_least_salary())
descending_salary()
for employee in list_employees:
    employee.print_all_info()