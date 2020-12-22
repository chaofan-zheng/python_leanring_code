def new_func(func):
    print("22")

    def wrapper():
        print("11")
        result = func()
        return result

    return wrapper


@new_func
def func01():
    print("hello")



@new_func
def func02():
    print("world")


func01()
func02()
