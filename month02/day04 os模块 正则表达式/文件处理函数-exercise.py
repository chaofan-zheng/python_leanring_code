"""
    删除主目录下，大小小于1k的文件
"""
def del_size_less_than_1k(path):
    import os
    file_name_list = os.listdir(path)
    for file_name in file_name_list:
        if os.path.getsize(path + "/"+file_name) < 1024:
            os.remove(path+"/"+file_name)

