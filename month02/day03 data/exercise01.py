"""
    一次读取5个字符，将file.txt文件从头到尾读取打印出来，打印内容与原文件保持一致
"""

file_name = "file.txt"
file_test = open(file_name,'rb')
while True:
    data = file_test.read(5)  #通常写2的n次方
    if not data:
        break
    print(data,end = "")
file_test.close()
