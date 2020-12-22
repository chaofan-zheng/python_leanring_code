"""
文件打开操作
"""

file = open("../day02_Linux/01", "r")
print(file)
file.close()

# print(open("../day02_Linux/01", "r").read())
# file = open("file.txt", "w")
# file.close()
file = open("file.txt", "a")
file.close()

print(file)

file_name = "file.txt"
file_test = open(file_name, "r")
data_test = file_test.read(10)
print(data_test)
data_test = file_test.read(8)
print(data_test)
data_test = file_test.read(10)  # 剩下的是空字符
print(data_test)
data_test = file_test.read(10)  # 剩下的是空字符
print(data_test)
file_test.close()

# 按行读取readline
file_test = open("file.txt", "r")
data_line = file_test.readline(5)
print(data_line)
data_line = file_test.readline(20)
print(data_line)
data_line = file_test.readline(20)
print(data_line)
file_test.close()

# readlines
file_test = open(file_name, "r")
data_line = file_test.readlines(14)
print(data_line)
file_test.close()

# 迭代获取
file_test = open(file_name, "r")
for line in file_test:
    print(line)
