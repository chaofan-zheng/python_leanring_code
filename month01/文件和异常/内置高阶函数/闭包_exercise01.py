"""
    使用闭包模拟以下情景
    在银行开户存入10000
    购买xx商品花了xx元
"""


def give_money_to_bank(money):
    print(f"银行账户里有{money}元")

    def buy_commodity(name, price):
        nonlocal money
        money -= price
        print(f"买了{name},花了{price}元，还剩{money}元")

    return buy_commodity


buy01 = give_money_to_bank(10000)
buy01("iphone12 pro 256G", 8999)
buy01("xxx",1000)
buy02 = give_money_to_bank(10000)
