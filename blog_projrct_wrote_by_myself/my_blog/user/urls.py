from django.urls import path
from . import views
urlpatterns = [
    path('sms', views.sms_view),
    path('<str:username>',views.UserView.as_view()),

]