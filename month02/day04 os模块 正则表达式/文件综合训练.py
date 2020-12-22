"""
    网络日志
    网络日志特征
    1. 每一段都是对一个设备的描述，段与段之间有空行
    2. 段的首单词，是设备名称

    设计一个程序，传入设备名称，得到address is 的值

    提示：
    1. 有些设备名字比较简单，有些比较复杂
    2. address 第一个

    思路：先得到段，再去做匹配。并且要有提示如果设备名称不在怎么办

"""


def find_internet_address(name):
    import re
    file_name = "log.txt"
    log = open(file_name).read()  # 记得关
    log_parts = log.split("\n\n")
    del log_parts[0]
    for part in log_parts:
        if name == re.match(r'\S+', part).group():
            internet_address = re.search(r'\w(?P<address> address is .+)', part)
            # address = re.search(r'\W (?P<address> address is .+)', part)
            if not internet_address:
                return "找不到该设备地址"
            else:
                return "Internet" + internet_address.group("address")

    return "找不到该设备名称"


def find_address(name):
    import re
    file_name = "log.txt"
    log = open(file_name).read()  # 记得关
    log_parts = log.split("\n\n")
    del log_parts[0]
    for part in log_parts:
        if name == re.match(r'\S+', part).group():
            address = re.search(r'\W (?P<address>address is .+)', part)
            if not address:
                return "找不到该设备地址"
            else:
                return address.group("address")
    return "找不到该设备名称"


print(find_address("BVI100"))
print(find_internet_address("BVI100"))


# 获取段落方法二：
def get_paragraph():
    file = open("log.txt")
    while True:
        info = ""
        for line in file:
            if line == '\n':
                break
            info += line
            if info:
                yield info
            else:
                file.close()
                return

# 获取地址正则表达式2
# pattern=r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"


