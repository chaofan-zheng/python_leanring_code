"""mysite3 URL Configuration

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
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('sports', views.sports_view),
    # news_url 相当于是一个变量，他的值是news
    path('news', views.news_view, name='news_url'),
    path('<int:num>', views.pagen_view, name='pagen_url'),
    path('test_static', views.test_static),
    # 再往下做分布式路由

    path('user/', include('user.urls')),
    path('music/', include('music.urls')),
    path('index',views.index2_view)
]
