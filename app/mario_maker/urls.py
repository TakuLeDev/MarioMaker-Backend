from django.urls import path
from .views import *

urlpatterns = [

    # =========================
    # Users
    # =========================

    

    path('user/signin/', user_signin, name='user_signin'),
    path('user/login/', user_login, name='user_login'),
    path('user/logout/', user_logout, name='user_logout'),

    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/delete/<pk>/', delete_user, name='delete_user'),
    path('user/<str:name>/', get_user, name='get_user'),

    # =========================
    # Levels
    # =========================

    path('levels/', create_level, name='create_level'),

    path('levels/latest/<int:nmbr>/', get_level_infos, name='get_level_infos'),

    #path('levels/latest/<int:nmbr>/<str:user_id>', get_level_infos, name='get_level_infos'),

    path('levels/<str:id>/json/', get_level_json, name='get_level_json'),

    path('levels/<str:lvl_id>/update/', update_level, name='update_level'),

    path('levels/<str:lvl_id>/delete/', delete_level, name='delete_level'),
]