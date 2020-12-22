filename = "programming"

with open(filename, "w") as file_object:  # open 函数的第二个实参"w"用的是写入模式
    file_object.write("I love programming! ")

with open(filename, "a+") as file_object:
    file_object.write("\nMe too!")

# w 写入模式    r 读取模式    a 附加模式（附加写）    r+ 读写模式    a+  附加读写
# "w" "r" 会清空原先的内容，"a" 不会
# Python 只能够将字符串写入文本文件。要将数值数据存储到文本文件中，必须要先使用函数str（）。
