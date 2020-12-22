"""
    假设在当前文件夹中有一个文件夹下有一个图片timg.jfif
    请编写一个函数，将该文件名传入，通过执行函数将其复制一份，到主目录下。
    注意：考虑到可能文件比较大，不允许一次性读取。
"""


def copy_to_home(file_name):
    with open(file_name, "rb") as file_object:
        home_file = open("../../../../../aiden_zcf/"+file_name, "wb")
        while True:
            line = file_object.readlines(10240)
            if not line:
                break
            home_file.writelines(line)
        home_file.close()


copy_to_home("exercise03.py")
