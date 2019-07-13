from django.urls import path

from . import views

urlpatterns = [
    path('', views.FriendListAPIView.as_view()),
]
