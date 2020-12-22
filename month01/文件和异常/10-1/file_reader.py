with open("pi_digits") as file_object:  #
    # with 在不再需要访问文件后关闭文件，让python自己去决定什么时候关闭。如果调用open(),Close(),如果程序存在bug，会导致文件打开了不会被关闭。
    # 使用with时，file_object文件只能在with代码区中使用（局部变量）
    contents = file_object.read()  # read()文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一 个空行。要删除多出来的空行，可在print 语句中使用rstrip()
    print(contents)

pi_digits = open("pi_digits").read()  # 这样也可以
print(pi_digits)

"""
逐行读取
"""
file_name = "pi_digits"
with open(file_name) as file_object:
    for line in file_object:
        print(line)  # 为什么会出现这么多空白行呢，是因为在这个文件中，每一行的末尾都有一个看不见的换行符，然而print语句也会加上一个换行符。
        # 如果说要消除这些空白行，可以使用rstrip函数

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# 因为使用with时，file_object文件只能在with代码区中使用，（出了代码区会关掉）所以如果要在with代码模块外访问文件内容，就需要使用一个列表存储。
"""
readlines函数会把行放在列表里储存
"""
with open(file_name) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())

pi_string = ""
for line in lines:
    pi_string += line.rstrip()  # 删除换行符，放在字符串中

print(pi_string)
print(len(pi_string))  # 打印字符串长度。
