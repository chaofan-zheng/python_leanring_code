"""
询问用户为什么喜欢变成，每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中
"""
filename = "guest"

while True:
    with open(filename,"a+") as file_object:
        content = str(input("Please input the reason why you like programming: "))
        if content == "":
            break
        file_object.write(content)
