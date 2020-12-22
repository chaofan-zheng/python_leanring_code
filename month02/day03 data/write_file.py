"""
    文件写方法示例
"""

file = open("file.txt", "wb")
file.write("hello ".encode())
file.close()

file = open("file.txt", "a")
file.write("makabaka\n")
file.close()

file = open("file.txt", "ab")
file.write("hello yigubigu\n".encode())
file.close()

data_list = [
    "接着奏乐",
    "接着舞"
]
file02 = open("file02.txt","a")
file02.writelines(data_list)


