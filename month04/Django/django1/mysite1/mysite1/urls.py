"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 新加
    # http://127.0.0.1:8000
    path('', views.page_index),  # 默认首页
    # http://127.0.0.1:8000/page/2003
    # 第三个参数就是给url的值起名称
    # 从语法的角度去理解，相当于pangen这个变量的值是'page/2003'
    path('page/2003', views.page_2003, name='pagen'),
    path('page/2004', views.page_2004),
    # path 转换器
    # 把数字通过关键字传参数传给num
    path('page/<int:num>', views.page_num),
    #     哪个path参数写在前面其实对它的显示也是有影响的，因为机制是遍历，先找到，先显示

    # str 与path的对比

    # path('page/<str:data>', views.page_data),

    # 练习1
    path('<int:num1>/<str:op>/<int:num2>',views.page_op),
    # 练习2
    re_path(r'^birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})$',views.birthday),
]
