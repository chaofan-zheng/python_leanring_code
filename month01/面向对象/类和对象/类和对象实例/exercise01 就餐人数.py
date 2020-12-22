class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐厅的名称为{self.name}，餐厅的类别的{self.type}")

    def open_restaurant(self):
        print("餐厅正在营业")

    def print_number_served(self):
        print(f"有{self.number_served}人在{self.name}就餐过")

    def set_number_served(self, new_number):
        if new_number > 0:
            self.number_served = new_number
        else:
            print("就餐人数不能小于0")


hidilao = Restaurant("海底捞", "hotpot")
hidilao.set_number_served(10000)
hidilao.print_number_served()
