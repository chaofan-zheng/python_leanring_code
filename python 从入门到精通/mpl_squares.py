import matplotlib.pyplot as plt

inputvalue = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 15, 25]
# linewidth 设置线宽
plt.plot(inputvalue, squares, linewidth=5)
# 字体大小 fontsize
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
# 设置刻度的样式，其中指定的axis，默认值是both，其余写"x","y",影响x轴y轴。labelsize影响标记刻度的字号。
plt.tick_params(axis="both", labelsize=14)

plt.show()
