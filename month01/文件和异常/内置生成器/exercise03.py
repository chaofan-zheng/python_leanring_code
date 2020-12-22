"""
练习 1：使用生成器表达式在列表中获取所有字符串list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
练习 2：在列表中获取所有整数,并计算它的平方.

"""

list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

data_str = (item for item in list01 if type(item) == str)
for item in data_str:
    print(item)

data_int = (item for item in list01 if type(item) == int)
for item in data_int:
    result = item**2
    print(result)
