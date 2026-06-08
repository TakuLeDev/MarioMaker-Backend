from django.urls import path
from .views import *

urlpatterns = [

    # =========================
    # Users
    # =========================

    path('users/<str:name>/', get_user, name='get_user'),

    path('users/signin/', user_signin, name='user_signin'),
    path('users/login/', user_login, name='user_login'),
    path('users/logout/', user_logout, name='user_logout'),

    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('users/<int:pk>/delete/', delete_user, name='delete_user'),

    # =========================
    # Levels
    # =========================

    path('levels/', create_level, name='create_level'),

    path('levels/latest/<int:nmbr>/', get_level_infos, name='get_level_infos'),

    path('levels/<int:id>/json/', get_level_json, name='get_level_json'),

    path('levels/<int:lvl_id>/update/', update_level, name='update_level'),

    path('levels/<int:lvl_id>/delete/', delete_level, name='delete_level'),
]