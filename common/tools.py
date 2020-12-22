"""

"""


def copy_to_home(path, file_name):
    """
    万物拷贝器（除了文件夹）
    :param path: 拷贝到的路径
    :param file_name: 要拷贝的文件名称（带格式）
    :return: none
    """
    with open(file_name, "rb") as file_object:
        home_file = open(path + file_name, "wb")
        while True:
            line = file_object.readlines(10240)
            if not line:
                break
            home_file.writelines(line)
        home_file.close()
