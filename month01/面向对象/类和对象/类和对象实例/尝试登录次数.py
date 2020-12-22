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


me = User("Chaofan", "Zheng", 19980823)
me.describe_user()
me.greet_user()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)
