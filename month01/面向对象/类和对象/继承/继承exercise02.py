"""
继承练习02
管理员
管理员是特殊用户，编写Admin的类，用来继承User类。添加一个privileges的属性，用于储存一个由字符串组成的列表，用show_privileges的方法
显示管理员的权限，创建一个Admin的实例，并且调用这个方法。

"""


class User:
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.login_attempts = 0
        self.password = 123456
        self.account = "Aiden_zcf"

    def describe_user(self):
        print(
            f"The user's first name is {self.first_name}, last name is {self.last_name}, birthday is {self.birthday}, account is {self.account}.")

    def greet_user(self):
        print(f"Morning, {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, birthday):
        super().__init__(first_name, last_name, birthday)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_priviledges(self):
        print(f"Admin's privileges{self.privileges}")


me = Admin("Chaofan", "Zheng", 19980823)
me.show_priviledges()
