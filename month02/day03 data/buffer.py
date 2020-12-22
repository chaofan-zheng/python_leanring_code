file = open("file.txt", "wb", buffering=10)
# 第十一个的时候写进去，buffering是缓冲区大小
while True:
    msg = input(">>")
    if not msg:
        break
    file.write(msg.encode())

file.close()

