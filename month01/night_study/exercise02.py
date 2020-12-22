"""
    不使用循环计算1+2+3+....+n
"""


# 使用递归的方法
class DiGuiCalculate:
    def di_gui(self, n):
        if n < 1:
            return 0
        return n + self.di_gui(n - 1)


di_gui_calculate = DiGuiCalculate()
print(di_gui_calculate.di_gui(10))


def di_gui(n):
    print(n, "<===1====>")
    if n > 0:
        di_gui(n - 1)
    print(n, '<===2====>')


di_gui(5)  # 外部调用后打印的结果是？

