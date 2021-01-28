from django.urls import path
from . import views
urlpatterns = [
    # 注意这个必须写到最上面
    # 而且在注册的时候要把sms作为一个关键字，不能注册
    path('sms',views.sms_view),
    # http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>',views.UserView.as_view()),
    # http://127.0.0.1:8000/v1/users/tedu/avatar
    path('<str:username>/avatar',views.user_avatar),
]