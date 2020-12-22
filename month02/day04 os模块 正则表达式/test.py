def find_address(name):
    import re
    file_name = "log.txt"
    log = open(file_name).read() # 记得关
    log_parts = log.split("\n\n")
    del log_parts[0]
    for part in log_parts:
        return re.match(r'\S+',part).group()


print(find_address("Loopback0"))