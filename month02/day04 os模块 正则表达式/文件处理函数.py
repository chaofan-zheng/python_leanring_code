"""
    文件处理函数
"""
import os

print("文件大小", os.path.getsize("../day03 data/my.log"))
print("文件大小", os.path.getsize("../.."))
print("文件列表", os.listdir(".."))
print("文件是否存在", os.path.exists("../day03 data/my.log"))
print("文件类型", os.path.isfile("../day03 data/my.log"))

# 文件大小 299
# 文件大小 448
# 文件列表 ['.DS_Store', 'day03 data', 'day02_Linux', 'day01 Linux', '第一次周测', 'day04 os模块 正则表达式']
# 文件是否存在 True
# 文件类型 True
