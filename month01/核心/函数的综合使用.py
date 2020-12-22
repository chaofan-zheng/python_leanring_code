# 参照day08 / homework / exercise06.py实现下列功能
# (1).定义函数, 打印所有员工信息,
# 格式：xx的员工编号是xx, 部门编号是xx, 月薪xx元.
# (2).定义函数, 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx, 部门编号是xx, 月薪xx元.
# (3).定义函数, 在部门列表中查找编号最小的部门
# (4).定义函数, 根据部门编号对部门列表降序排列
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}
# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]


def print_info(department_num, info):
    """
    按照第一层字典的键，值打印员工的所有信息
    :param department_num: 部门编号
    :param info: 信息的字典
    :return: none
    """
    print("%s的员工编号是%d,部门编号是%d,月薪%d元." % (info["name"], info["did"], department_num, info["money"]))


def print_all_info():
    """
    打印所有员工信息
    :return: none
    """
    for department_num, info in dict_employees.items():  # 这里和上面的变量比较，只是多了一个循环
        print_info(department_num, info)


def print_salary_bigger_than_2w():
    """
    打印所有工资大于两万的员工信息
    :return: none
    """
    for department_num, info in dict_employees.items():
        if info["money"] > 20000:
            print_info(department_num, info)


def find_the_smallest_department():
    """
    找到编号最小的部门
    :return: 部门名称
    """
    smallest_department = list_departments[0]["did"]
    index = 0
    for i in range(len(list_departments)):
        if list_departments[i]["did"] < smallest_department:
            smallest_department = list_departments[i]["did"]
            index += 1
        return list_departments[index]["title"]
# 其实是这一题的解题思路最难，因为要找did最小，但是不能通过did返回整个员工信息，就给整个员工信息加一个索引（因为是嵌套在列表里面）
# 通过索引 定位员工信息

def rank_department():
    """
    根据部门编号进行排序
    :return: none
    """
    for r in range(len(list_departments) - 1):
        for c in range(r + 1, len(list_departments)):
            if list_departments[r]["did"] < list_departments[c]["did"]:
                list_departments[r]["did"], list_departments[c]["did"] = list_departments[c]["did"], \
                                                                         list_departments[r]["did"]


print_all_info()
print_salary_bigger_than_2w()
print(find_the_smallest_department())
rank_department()
print(list_departments)
