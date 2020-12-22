"""
1. 员工信息管理系统
    添加/显示/删除/修改
    class Employee:
        def __init__(self, eid, did, name, money):
            self.eid = eid
            self.did = did
            self.name = name
            self.money = money

"""


class EmployeeModel:
    def __init__(self, name="", did=0, salary=0, eid=0):
        self.did = did
        self.salary = salary
        self.name = name
        self.eid = eid

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid}，部门编号是{self.did}，工资是{self.salary}"

    def __eq__(self, other):
        if self.eid == other.eid:
            return True


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("输入1添加员工信息")
        print("输入2显示员工信息")
        print("输入3删除员工信息")
        print("输入4修改员工信息")

    def __select_menu(self):
        choice = input("请输入你的选择")
        if choice == "1":
            self.__add_staff_info()
        if choice == "2":
            self.__show_staff_info()
        if choice == "3":
            self.__del_staff()
        if choice == "4":
            self.__update_staff_info()

    def get_int(self, message):
        while True:
            try:
                number = int(input(message))
            except:
                print("请输入一个整数")
            else:
                return number

    def __add_staff_info(self):
        name = input("请输入员工姓名")
        did = self.get_int("请输入员工部门编号")
        salary = self.get_int("请输入员工工资")
        employee = EmployeeModel(name=name, did=did, salary=salary)
        self.__controller.add_employee(employee)
        print("添加成功啦")

    def __show_staff_info(self):
        for staff in self.__controller.employee_list:
            print(staff)

    def __del_staff(self):
        eid = self.get_int("请输入要删除的员工编号")
        if self.__controller.del_employee(eid):
            print("删除成功啦")
        else:
            print("删除失败啦")

    def __update_staff_info(self):
        staff = EmployeeModel()
        staff.eid = self.get_int("请输入要修改的员工的员工编号")
        staff.did = self.get_int("请输入要修改的部门编号")
        staff.name = input("请输入要修改的员工姓名")
        staff.salary = self.get_int("请输入要修改的员工工资")
        if self.__controller.update_employee(staff):
            print("修改成功啦")
        else:
            print("修改失败啦")


class EmployeeController:
    def __init__(self):
        self.__employee_list = []
        self.__start_eid = 1000

    @property
    def employee_list(self):
        return self.__employee_list

    def add_employee(self, employee):
        employee.eid = self.__start_eid
        self.__start_eid += 1
        self.__employee_list.append(employee)

    def del_employee(self, eid):
        for employee in self.__employee_list:
            if employee.eid == eid:
                self.__employee_list.remove(employee)
                return True
            return False

    def update_employee(self, staff):
        for employee in self.__employee_list:
            if employee.eid == staff.eid:
                employee.__dict__ = staff.__dict__
                return True
            return False


view = EmployeeView()
view.main()
