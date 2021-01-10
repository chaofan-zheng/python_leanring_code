from django.urls import path

from . import views

urlpatterns = [
    # 127.0.01:8000/user/index
    path('index',views.index_view)
]