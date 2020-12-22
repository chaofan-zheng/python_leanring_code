# 定义函数,在手机列表中查找所有白色的手机
#    定义函数,在手机列表中查找品牌是"华为2"的手机对象(如果有多个返回第一个)
#    定义函数,在手机列表中查找单价小于6000的所有手机
class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    # 1


list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]


def brand_finder():
    result_list = []
    for item in list_phones:
        if item.brand == "华为2":
            result_list.append(item)
    return result_list


for i in range(len(brand_finder())):
    print((brand_finder()[i].brand, brand_finder()[i].price, brand_finder()[i].color))
