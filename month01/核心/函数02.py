# 定义函数,根据总两数,计算几斤零几两.:
#  提示：使用容器包装需要返回的多个数据
# total_liang = int(input("请输入两:"))
# jin = total_liang // 16
# liang = total_liang % 16
# print(str(jin) + "斤零" + str(liang) + "两")

def jin_liang_calculator(total_liang):
    """
    输入总两数，输出对应的斤，两
    :param total_liang: 总两数
    :return: 斤，两
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang


total_liang = int(input("请输入两:"))
result = jin_liang_calculator(total_liang)
print(f"{result[0]}斤零{result[1]}两")
