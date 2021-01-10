from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html1 = """
<form method='get' action="/test_get">
    <p>
        姓名：<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
    
</form>"""

html2 = """
<form method='post' action="/test_post">
    <p>
        姓名：<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
    
</form>
"""


def test_get(request):
    # 1. 后段收到前端提交的查询字符串
    # uname = request.GET['uname']
    # 要求查询字符串中存在名称为uname的数据
    # 这种方式容易产生错误

    # 2.换一种方式获取，试着获取，没有也不报错，值为none而已
    # 默认值不写为none，第二个参数为默认值
    # uname = request.GET.get('uname','tedu')
    # print(uname)

    # ?a=100&b=100&c=100&a=200
    # 3.如果有多个值，只会拿a
    # print(request.GET.get('a')) # 200

    # ?a=100&b=100&c=100&a=200
    # 4.如果一个名称有多个值 getlist会返回列表
    print(request.GET.getlist('a'))  # ['100', '200']
    return HttpResponse(html1)


def test_post(request):
    if request.method == 'GET':
        return HttpResponse(html2)
    elif request.method == 'POST':
        uname = request.POST['uname']
        # 与GET类似但是POST可以强拿，也可以温柔拿
        # request.POST.get['uname',none]
        # request.POST.getlist['uname']
        return HttpResponse(f'劳资欢迎你{uname}')


def birthday(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    # http://127.0.0.1:8000/birthday?year=1998&month=08&day=23
    return HttpResponse(f'您的生日：{year}年{month}月{day}日')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showData(self):
        return f'姓名:{self.name}, 年龄:{self.age}'


def hello():
    return "劳资欢迎你！"


def test_html(request):
    # 方式一
    # 返回一个模板页
    # t = loader.get_template("test_html_blank.html")
    # html = t.render()
    # return HttpResponse(html)

    # 方式二
    # 直接返回render
    # dict1 = {}
    # dict1['name'] = 'aid2010'
    # dict1['count'] = '伍佰'
    # dict1['cities'] = ['北京', '上海', '天津', '重庆']
    # dict1['distribute'] = {'西安': 100, '杭州': 100}
    # dict1['person1'] = Person('干饭王', 22)
    # dict1['function1'] = hello
    # # 来点特殊的
    # # 为什么不行，因为Django框架为了保护用户计算机不受攻击，不会让浏览器执行这个代码
    # dict1['script'] = '<script>alert("想不到吧，还能传JS文本")</script>'
    # return render(request, "test_html_blank.html", dict1)

    # 终极解决方案：最推荐的方案
    # 方式三
    name = 'aid2010'
    count = '3'
    cities = ['北京', '上海', '天津', '重庆']
    distribute = {'西安': 100, '杭州': 100}
    person1 = Person('干饭王', 22)
    function1 = hello
    # 来点特殊的
    # 为什么不行，因为Django框架为了保护用户计算机不受攻击，不会让浏览器执行这个代码
    script = '<script>alert("想不到吧，还能传JS文本")</script>'
    # 用于for循环
    people = ['关羽', '张飞', '赵云', '黄忠', '马超']
    return render(request, "test_html_blank.html", locals())


# 计算器案例：
# 1. 在templates目录下添加模板页面 test_calc.html 写好html内容 客户端运行的时候会将数据往服务端传
# 2. urls 进行任务的分配，调用view里的处理函数。urls.py的path和html form表单中的main要相同
# 3. 写view函数处理浏览器提交的数据，view函数的第一个参数是HttpResponse对象
# 4. view将处理好的数据传给template(html)
# 5. 修改template，进行更新显示
def test_calc(request):
    if request.method == "GET":
        return render(request, "test_calc.html")
    elif request.method == "POST":
        op = request.POST['op']
        x = request.POST['x']
        y = request.POST['y']

        # test

        # 判断数值为空
        if not x or not y:
            return HttpResponse('请输入数据')
        try:
            x = int(x)
            y = int(y)
        except:
            return HttpResponse('请输入一个整数值')
        if op == 'add':
            res = x + y
        elif op == 'sub':
            res = x - y
        elif op == 'mul':
            res = x * y
        elif op == 'div':
            res = x / y
        return render(request, "test_calc.html", locals())
