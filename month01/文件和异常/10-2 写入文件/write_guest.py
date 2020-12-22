filename = "guest"
# with open(filename,"a+") as file_object:
    # file_object.write(str(input("please input your name:")))

while True:
    with open(filename, "a") as file_object:
        content = str(input("please input your name:"))
        if content == "":
            break
        file_object.write(content + "\n")
        print("hello" + content)
