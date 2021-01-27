"""ddblog URL Configuration

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
from user import views as user_views  # 为了防止与主目录下的views冲突，进行重命名
from btoken import views as btoken_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cors', views.test_cors),
    path('test_cors_server', views.test_cors_server),
    # 博客项目路由设置
    # 基于CBV
    # 模块函数名.试图类.as_view()
    # 在as_view()里针对不同请求方式，在试图类中去查找对应的类的方法（封装在django里面）找到调用，没找到直接报异常
    # 异常码405 请求的方法不存在
    path('v1/users', user_views.UserView.as_view()),  # 类中的函数
    # 在urls中 分布式陆游模块
    path('v1/users/',include('user.urls')),

    path('v1/tokens',btoken_views.TokenView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)