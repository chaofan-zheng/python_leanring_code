list01 = [65, 67, 3, 75, 2, 56, 74, 222]

# for item in list01:
#     if item > 10:
#         item = 10
# print(list01)
#
# for i in range(len(list01)):
#     if list01[i]>10:
#         list01[i]=10
# print(list01)

for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 10

print(list01)

