"""
    把文件夹设置为根目录，导入的时候能有提示
    使用模块的时候也能够有提示
"""
# import module01
#
# module01.func01()

from module01 import func01

func01()

from module01 import *    # 有缺陷 会覆盖

