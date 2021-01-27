from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/v1/users/tedu(<str:username>)
    path('<str:username>',views.UserView.as_view()),
    # 专门用来用户头像上传.对于头像上传，用一个单独的函数来用作用户的头像上传，就不用类了
    path('<str:username>/avatar',views.user_avatar),

]