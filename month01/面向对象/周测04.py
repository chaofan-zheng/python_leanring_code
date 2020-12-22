"""
    假设一本书的定价是25元，双十一网上买打了6折。运费是一本书3元，每加一本加0.75元。60本书的总价是多少，均价是多少，马云亏多少钱？
    算数运算符
    + -　* / //　％　＊＊
"""


def func01(book_num):
    total_price = book_num * 25 * 0.6 + 3 + 0.75 * (book_num - 1)
    average_price = total_price/book_num
    lose_money = (25 - average_price)*(book_num)
    return f"60本书的总价是{total_price}，均价是{average_price}，马云亏{lose_money}"


print(func01(60))