from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls', 'user'), namespace='user'),
    path('friend/', include('api.friend.urls', 'friend'), namespace='friend'),
    path('letter/', include('api.letter.urls', 'letter'), namespace='letter'),
]