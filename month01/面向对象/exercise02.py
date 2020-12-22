# 练习:将下列面向过程的代码改为面向对象代码.
#     备注:参照下列思想完成
# 步骤:1. 根据字典创建类
#     2. 修改商品列表(字典 -> 自定对象)
#     3. 修改函数(对数据的操作)

# 面向过程:
# list_orders = [
#     {"cid": 1001, "count": 1},
#     {"cid": 1002, "count": 3},
#     {"cid": 1005, "count": 2},
# ]
# def print_orders():
#     for order in list_orders:
#         print("商品编号是:%d,购买数量是:%d"%(order["cid"],order["count"]))
# 面向对象:

class Orders:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count

    def print_orders(self):
        print("商品编号是：%d,购买数量是：%d" % (self.cid, self.count))


order1 = Orders(1001, 1)
order2 = Orders(1002, 3)
order3 = Orders(1005, 2)
order1.print_orders()


# -----------------------练习开始-------------------------------
class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


# 商品列表
list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1001, "屠龙刀", 10000),
]


# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.

def print_single_commodity(commodity):
    print("商品编号%d,商品名称%s,商品单价%s" % (commodity.cid, commodity.name, commodity.price))


def print_all_commodity():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)


# 2.  定义函数,打印商品单价小于2万的商品信息
def print_less_than_20000():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)


# 4. 查找最贵的商品(使用自定义算法,不使用内置函数)
def find_the_most_expensive():
    most_expensive = list_commodity_infos[0].price
    for commodity in list_commodity_infos:
        if commodity.price > most_expensive:
            most_expensive = commodity.price
            most_expensive_result = commodity
    return most_expensive_result


# 5. 根据单价对商品列表降序排列

def descending_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], \
                                                                   list_commodity_infos[r]


print_all_commodity()
print_less_than_20000()
result = find_the_most_expensive()
print_single_commodity(result)
descending_by_price()
for item in list_commodity_infos:
    print_single_commodity(item)