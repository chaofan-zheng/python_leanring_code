# 采用相对路径读取文件
with open("text_file/text_file") as file_object01:  # 没有第一个斜杠
    content01 = file_object01.read()
    print(content01)

# 采用绝对路径读取文件
with open("/users/aiden_zcf/PycharmProjects/Tmooc/文件和异常/10-1/text_file/text_file") as object02: # 第一个斜杠不能省略
    content02 = object02.read()
    print(content02)