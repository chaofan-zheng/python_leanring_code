"""
    编写一个程序，每隔2s向文件my.log中写入一行内容，程序死循环不会停止，当强行结束程序，重新启动能够继续写入内容，并序号衔接
    sleep(
"""
import time


def my_log():
    file_name = "my.log"
    file = open(file_name, "ab+")
    file.seek(0)
    count = 0
    for line in file:
        if not line:
            break
        else:
            count += 1
    while True:
        count += 1
        str_time = time.strftime("%y-%m-%d %H:%M:%S")
        file.write(f"{count}. {str_time}\n".encode())
        file.flush()
        time.sleep(2)


my_log()
