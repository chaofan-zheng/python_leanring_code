"""
练习 1：不改变插入函数与删除函数代码，为其增加验证权限的功能

"""


def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        result = func(*args, **kwargs)
        return result

    return wrapper


@verify_permissions
def insert(p1, p2):
    print("插入")
    print(p1 + p2)
    return 100


@verify_permissions
def delete(p1, p2, p3, p4):
    print("删除")
    print(p1 + p2, p3 - p4)
    return 404


# insert = verify_permissions(insert)
print(insert(1, 2))
# delete = verify_permissions(delete)
print(delete(1, 2, p3=100, p4=56))
