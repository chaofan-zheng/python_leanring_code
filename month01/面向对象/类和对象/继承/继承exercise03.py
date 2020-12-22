"""
练习03
编写一个为Privilege的类，只有一个属性privilege，存贮练习02重的字符串列表，然后将方法show_privileges放到这个类里面
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


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin's privileges{self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, birthday):
        super().__init__(first_name, last_name, birthday)
        self.privileges = Privileges()


me = Admin("Chaofan", "Zheng", 19980823)
me.privileges.show_privileges()
