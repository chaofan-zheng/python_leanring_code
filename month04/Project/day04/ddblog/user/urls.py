from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>',views.UserView.as_view()),
    # http://127.0.0.1:8000/v1/users/tedu/avatar
    path('<str:username>/avatar',views.user_avatar)
]