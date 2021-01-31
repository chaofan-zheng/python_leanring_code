from django.urls import path
from . import views
urlpatterns = [
    path('<int:topic_id>',views.message_view)
]