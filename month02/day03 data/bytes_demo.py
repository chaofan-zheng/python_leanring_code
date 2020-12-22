"""
字节串使用示例
    所有字符串都能转化为字节串，但不是所有字节串都能转化为字符串。
"""

# 定义一个字节串变量
b = b"hello world"  # 用于ASCii
print(type(b))

# 定义一个非ASCII字节串变量
b1 = "你好".encode()
print(b1)
x1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode() # 等同于 x1 = b1.decode()
print(x1)




file = open("file.txt")
file_object = file.read()
file_list = file_object.split("\n")
print(file_list)
number = len(file_list)



