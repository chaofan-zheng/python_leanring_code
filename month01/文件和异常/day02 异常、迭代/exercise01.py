"""
    练习：创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入。
效果： score  = get_score()
       print("成绩是：%d"%score)
"""


def get_score():
    count = 0
    while True:
        try:
            score = int(input("请输入成绩"))
        except:
            print("必须输入一个整数")
        else:
            print(f"成绩是{score}")
        finally:
            count+=1
            print(f"这是第{count}次运行")

get_score()