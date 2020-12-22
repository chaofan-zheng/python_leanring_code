# format函数
age = 22
name = "Kitty"
print("*" * 50)
print("{0} is {1} years old.".format(name, age))
print("{} 的年龄是{}".format(name, age))
print("{name} 的年龄是{age}".format(name=name, age=age))

# 与f-string都能互换
num = 1 / 3
print(f"{num:.3} is a decimal")  # 0.333 is a decimal
print("{0:.3} is a decimal".format(1 / 3))  # 0.333 is a decimal
print("{0:_^11} is a 5 length".format(name))  # ___Kitty___ is a 5 length
print(f"{name:_^11} is a 5 length")  # ___Kitty___ is a 5 length
print("{0:<11} is a 5 length".format(name))  # Kitty       is a 5 length
print(f"{name:<11} is a 5 length")  # Kitty       is a 5 length

# \t为tab
format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))

id, name, english, python, c, total = ("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩")
a = f"{id:^6}{name:^12}\t{english:^8}\t{python:^10}\t{c:^10}\t{total:^10}"
print(a)

# get 函数
dict01 = {"a": 97, "b": 98}
# print(dict01["c"]) # 报错
print(dict01.get("c"))  # None
print(dict01.get("c", 99))  # 99
print(dict01)  # 没有c，没有99
dict01["c"] = 100
print(dict01.get("c", 99))  # 100
