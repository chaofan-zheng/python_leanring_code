"""
扩展重写
"""


class StaffManager:
    def calculate_salary(self):
        pass


class Staff:
    def __init__(self, basic_wage):
        self.basic_wage = basic_wage

    def calculate_salary(self):
        return self.basic_wage


class Programmer(Staff):

    def __init__(self, basic_wage, bouns):
        super().__init__(basic_wage)
        self.bouns = bouns

    def calculate_salary(self):
        return super().calculate_salary() + self.bouns


giao = Programmer(5, 10)
print(giao.calculate_salary())

staff = Staff(10)
print(staff.calculate_salary())  # 不会影响到父类方法
