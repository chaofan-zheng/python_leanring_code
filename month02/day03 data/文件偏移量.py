"""
文件偏移量
"""

file = open("file.txt", "wb+")

file.write("2020-11-30".encode())
file.seek(-2,1)
file.write("28".encode())
file.seek(0)
date = file.read()
print(date)

file.close()

file01 = open("modified_timg.jpg", "wb+")
file02 = open("timg.jpg", "wb+")
file02.seek(10240,0)
file01.write(file02.read())
