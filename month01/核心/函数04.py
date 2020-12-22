"""
创建函数,根据课程阶段计算课程名称.
number = input("请输入课程阶段数：")
if number == "1":
    print("Python语言核心编程")
elif number == "2":
    print("Python高级软件技术")
elif number == "3":
    print("Web全栈")
elif number == "4":
    print("网络爬虫")
elif number == "5":
print("数据分析、人工智能")

"""


def find_course(number):
    """

    :param number:
    :return:
    """
    if number == "1":
        return "Python语言核心编程"
    if number == "2":
        return "Python高级软件技术"
    if number == "3":
        return "Web全栈"
    if number == "4":
        return "网络爬虫"
    return ("数据分析、人工智能")


number = input("请输入课程阶段数：")
print(find_course(number))


# 答案

def get_cousre_name(number):
    dict_course = {
        1: "Python语言核心编程",
        2: "Python高级软件技术",
        3: "Web全栈",
        4: "网络爬虫",
        5: "数据分析、人工智能"
    }
    return dict_course[number]


print(get_cousre_name(7))