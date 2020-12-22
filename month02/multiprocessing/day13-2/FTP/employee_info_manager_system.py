class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return "%s的员工编号是%d,部门编号是%d,工资是%d" % (self.name, self.eid, self.did, self.money)

    # 指定比较相同的依据
    def __eq__(self, other):
        return self.eid == other.eid

class EmployeeView:

    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("按1键录入员工信息")
        print("按2键显示员工信息")
        print("按3键删除员工信息")
        print("按4键修改员工信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_employee_info()
        elif item == "2":
            self.__display_employees()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__modify_employee()

    def __input_employee_info(self):
        emp = EmployeeModel()
        emp.name = input("请输入员工姓名:")
        emp.did = int(input("请输入部门编号:"))
        emp.money = int(input("请输入员工薪资:"))
        self.__controller.add_employee_info(emp)
        print("添加员工生成功喽")

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_employees(self):
        for item in self.__controller.list_employees:
            print(item)

    def __delete_employee(self):
        eid = int(input("请输入需要删除的员工编号:"))
        if self.__controller.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        emp = EmployeeModel()
        emp.eid = int(input("请输入员工编号:"))
        emp.name = input("请输入员工姓名:")
        emp.did = int(input("请输入部门编号:"))
        emp.money = int(input("请输入员工薪资:"))
        if self.__controller.update_employee_info(emp):
            print("更新成功")
        else:
            print("更新失败")

class EmployeeController:
    """
        学生信息的控制
    """

    def __init__(self):
        self.__list_employees = []
        self.__start_id = 1001  # 开始编号

    # 只读属性
    @property
    def list_employees(self):
        return self.__list_employees

    def add_employee_info(self, emp_target):
        emp_target.eid = self.__start_id
        self.__start_id += 1
        self.__list_employees.append(emp_target)

    def remove_employee(self, eid):
        emp =EmployeeModel(eid)
        if emp in self.__list_employees:
            self.__list_employees.remove(emp)
            return True
        else:
            return False

    def update_employee_info(self, new_emp):
        for item in self.__list_employees:
            if item.eid == new_emp.eid:
                item.__dict__ = new_emp.__dict__
                return True
        return False

# 入口
view = EmployeeView()
view.main()
