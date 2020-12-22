"""
2，定义函数，根据输入的字符串（只有字母和数字），分别统计出其中英文字母、数字的个数。
"""

# 方法一
target = "asdhfk1213"
num_int = 0
num_str = 0
for item in target:
    try:
        int(item)
    except ValueError:
        num_str += 1
    else:
        num_int += 1

print(f"字符个数{num_str}")
print(f"数字个数{num_int}")


# 方法二
num_int = 0
num_str = 0
for item in target:
    if item.isalpha():
        num_str += 1
    elif item.isdigit():
        num_int += 1
print(f"字符个数{num_str}")
print(f"数字个数{num_int}")

