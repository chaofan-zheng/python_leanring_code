"""
    创建一个只执行除法运算的简单计算器
"""
print("Give me two numbers, and I'll divede them")
print("Enter 'q' to quit ")

while True:
    first_num = int(input("\n First number"))
    if first_num == "q":
        break
    second_num = int(input("\n Second number"))
    answer = first_num/second_num
    print(answer)
