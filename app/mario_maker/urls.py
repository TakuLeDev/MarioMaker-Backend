from django.urls import path
from .views import get_user, create_user, user_detail

urlpatterns = [
    path('get_name/<str:name>', get_user, name='get_user'),
    path('user/create', create_user, name='create_user'),
    path('get_pk/<int:pk>', user_detail, name='user_detail')
]