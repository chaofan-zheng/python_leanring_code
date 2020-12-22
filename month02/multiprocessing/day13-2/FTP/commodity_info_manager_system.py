"""
    步骤
    一.创建View类
        1. 定义函数,显示菜单
        2. 定义函数,选择菜单
        3. 因为需要输入1键录入学生信息,所以定义函数,录入学生信息
        4. 因为录入了多个信息(姓名/年龄..),所以创建Model类
        5. 因为数据准备完毕后,需要由控制器进行处理,所以创建Controller类
        6. 因为需要调用控制,所以创建构造函数
        7. 为了让入口代码方便使用,所以创建main函数
        8. 因为需要输入2键显示学生信息,所以定义函数,显示学生信息.
        9. 因为需要输入3键删除学生信息,所以定义函数,显示删除信息.

    二.创建Model类
        1. 定义实例变量(姓名/年龄)
        2. 因为显示学生默认是内存地址,所以重写__str__函数
        3. 因为移除学生信息自动调用__eq__函数,所以进行重写

    三.创建Controller类
        1. 定义函数,添加学生信息
        2. 定义构造函数,添加私有实例变量:学生列表和开始编号
        3. 定义只读属性:学生列表
        4. 定义移除学生信息函数
"""


class CommodityModel:
    """
        商品数据模型
    """

    def __init__(self, cid=0, name="", price=0):
        self.cid = cid  # 商品编号
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}的商品编号是{self.cid},价格是{self.price}"

    def __eq__(self, other):
        return self.cid == other.cid


class CommodityView:
    """
        商品界面逻辑
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity_info()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity_info(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity_info(commodity)
        print("添加成功")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for item in self.__controller.list_commoditys:
            print(item)

    def __delete_commodity(self):
        cid = int(input("请输入需要删除的商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        commodity = CommodityModel()
        commodity.cid = int(input("请输入需要修改的商品编号:"))
        commodity.name = input("请输入需要修改的商品名称:")
        commodity.price = int(input("请输入需要修改的商品单价:"))
        if self.__controller.update_commodity(commodity):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        商品业务逻辑
    """

    def __init__(self):
        self.__list_commoditys = []
        self.__start_id = 1000

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity_info(self, commodity):
        """

        :param commodity:
        :return:
        """
        commodity.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(commodity)

    def remove_commodity(self, cid):
        """
            移除商品信息
        :param cid: 商品编号
        :return: 是否移除成功,True表示移除成功,False表示移除失败
        """
        commodity = CommodityModel(cid)
        if commodity in self.__list_commoditys:
            self.__list_commoditys.remove(commodity)
            return True
        return False

    def update_commodity(self, new_commodity):
        """
            修改商品信息
        :param new_commodity:新商品
        :return:是否修改成功
        """
        for item in self.__list_commoditys:
            if item.cid == new_commodity.cid:
                item.__dict__ = new_commodity.__dict__
                return True
        return False


view = CommodityView()
view.main()
