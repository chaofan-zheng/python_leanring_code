from bll import HouseManagerController

"""
按1显示所有房源信息
按2显示总价最高的房源信息
按3键显示面积最小的房源信息
按4根据总价升序显示房源信息
按5根据面积降序显示房源信息
按6键查找所有户型信息 
   3室1厅    x个
   4室2厅    x个
"""


class HouseManagerView:
    def __init__(self):
        self.controller = HouseManagerController()

    def show_menu(self):
        print("输入1显示房源信息")
        print("输入2显示总价最高的房源信息")
        print("输入3显示面积最小的房源信息")
        print("按4根据总价升序显示房源信息")
        print("按5根据面积降序显示房源信息")
        print("按6查找所有户型信息 ")

    def select(self):
        choice = input("请输入你的选择")
        if choice == "1":
            self.controller.show_all_info()
        if choice == "2":
            self.controller.show_highest_price_info()
        if choice == "3":
            self.controller.show_smallest_area_info()
        if choice == "4":
            self.controller.ascending_by_total_price()
        if choice == "5":
            self.controller.descending_by_area()
        if choice == "6":
            self.controller.show_all_house_type_info()

    def main(self):
        view = HouseManagerView()
        while True:
            view.show_menu()
            view.select()
