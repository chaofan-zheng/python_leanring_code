"""
    请在屏幕上使用input函数，输入一首古诗
    写入到file_poesy,每次input舒服一句。
"""



file_name = "file_poesy"
poesy = open(file_name, "w")
count = 0
while True:
    count += 1
    content = input(F"请输入诗歌的第{count}句")
    if not content:
        break
    poesy.write(content + "\n")
print("end")
poesy.close()


