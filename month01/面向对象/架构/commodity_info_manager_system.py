"""
创建商品管理系统
    完成
    (1) 录入商品信息 (商品编号由c处理）
    (2) 存储商品信息，显示商品信息。
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"商品的名字是{self.name}，价格是{self.price}，编号是{self.cid}"

    def __eq__(self, other):
        if self.cid == other.cid:
            return True


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()  # 为什么不用

    def __display_menu(self):
        print("1) 输入商品信息")
        print("2) 显示商品信息")
        print("3) 删除商品信息")
        print("4) 修改商品信息")

    def __select_menu(self):
        item = input("请输入选项")
        if item == "1":
            self.__input_commodity_info()
        elif item == "2":
            self.__show_all_commodity_info()
        elif item == "3":
            self.__del_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity_info(self):  # 把它变成私有变量，是一个封装的意识。
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称")
        commodity.price = input("请输入商品价格")
        # controller = CommodityController()   不可以这么写，这么写每一次调用input这个函数的时候，都会创建一个新的controller。
        self.__controller.add_commodity_info(commodity)
        print("添加成功")

    def __show_all_commodity_info(self):
        for commodity in self.__controller.list_commodity:
            print(commodity)

    def main(self):
        """

        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __del_commodity(self):
        commodity_cid = int(input("输入要删除的商品编号："))
        if self.__controller.del_commodity(commodity_cid):
            print("成功删除了")
        else:
            print("删除失败了")

    def __modify_commodity(self):
        commodity_modified = CommodityModel()
        commodity_modified.cid = int(input("请输入需要修改的商品编号"))
        commodity_modified.name = input("请输入需要修改的商品名称")
        commodity_modified.price = int(input("请输入需要修改的商品价格"))
        if self.__controller.modify_commodity(commodity_modified):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    def __init__(self):
        self.__list_commodity = []
        self.__start_cid = 1000

    @property
    def list_commodity(self):
        return self.__list_commodity

    def add_commodity_info(self, commodity):
        commodity.cid = self.__start_cid
        self.__start_cid += 1
        self.__list_commodity.append(commodity)

    def del_commodity(self, commodity_cid):
        """

        :return: True or False
        """
        commodity_target = CommodityModel(cid=commodity_cid)
        if commodity_target in self.__list_commodity:  # 用属性或者私有变量都可以 但是在类里面，用私有变量比较好
            self.__list_commodity.remove(commodity_target)
            return True  # 移除成功
        return False  # 移除失败

    def modify_commodity(self, commodity_modified):
        for commodity in self.__list_commodity:
            if commodity.cid == commodity_modified.cid:
                commodity.__dict__ = commodity_modified.__dict__
                return True
            return False



view = CommodityView()
view.main()
