from django.shortcuts import render


def function1():
    return 'This is a function in views, which can be transported to templates'


def my_test(request):
    test_list = ['list item 1', 'list item 2', 'list item 3']
    test_dict = {'a': 'dict item 1', 'b': 'dict item 2'}
    my_class = MyClass()
    func = function1
    return render(request, 'my_test.html', locals())


class MyClass():
    def __init__(self):
        self.property1 = "property_value1"
        self.property2 = "property_value2"

    def function_in_my_class(self):
        return 'This is a function which return a string in my class'
