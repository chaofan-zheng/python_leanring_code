# import time
# a = time.localtime()
# print(a)

file = open("test", "r")
# file_lines = file.readlines()

# for line in file:
#     print(line)
#
# for line in file_lines:
#     print(line)

while True:
    data = file.read(5)
    print(data)
    if not data:
        break
