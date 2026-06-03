from django.urls import path
from .views import *

urlpatterns = [

    #region user

    path('user/get_name/<str:name>', get_user, name='get_user'),
    path('user/signin', user_signin, name='user_signin'),
    path('user/get_pk/<int:pk>', user_detail, name='user_detail'),

    #endregion

    #region level

    path('levels/level/create', create_level, name='create_level'),

    #endregion
]