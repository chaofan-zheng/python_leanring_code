from django.urls import path
from . import views

urlpatterns = [
    # path('result/', views.),
    path('jump/', views.JumpView.as_view()),
    path('result/', views.ResultView.as_view()),
]