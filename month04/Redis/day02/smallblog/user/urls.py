from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:uid>',views.user_detail),
    path('update/<int:uid>',views.user_update),
]
