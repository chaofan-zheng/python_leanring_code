"""
练习01
1，定义函数根据客户输入的值，计算s=a+aa+aaa+aaaa+aa...a的值.
例如: 输入2和5，结果s=2+22+222+2222+22222

"""

def special_calculator(x,y):
    num_initial = 0
    result_num = 0
    for i in range(y):
        num_initial += 10 ** i
        result_num += num_initial * x
    return result_num


print(special_calculator(2, 3))
