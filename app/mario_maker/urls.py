from django.urls import path
from .views import get_user, create_user

urlpatterns = [
    path('user/get/', get_user, name='get_user'),
    path('user/create', create_user, name='create_user')
]