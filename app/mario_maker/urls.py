from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [

    # =========================
    # Users
    # =========================

    

    path('user/signin/', user_signin, name='user_signin'),
    #path('user/login/', user_login, name='user_login'),
    path('user/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/logout/', user_logout, name='user_logout'),

    path('user/<uuid:pk>/', user_detail, name='user_detail'),
    path('user/delete/<uuid:pk>/', delete_user, name='delete_user'),
    path('user/<str:name>/', get_user, name='get_user'),

    # =========================
    # Levels
    # =========================

    path('levels/', create_level, name='create_level'),

    path('levels/latest/<int:nmbr>/', get_level_infos, name='get_level_infos'),

    #path('levels/latest/<int:nmbr>/<str:user_id>', get_level_infos, name='get_level_infos'),

    path('levels/<uuid:id>/json/', get_level_json, name='get_level_json'),

    path('levels/<uuid:lvl_id>/update/', update_level, name='update_level'),

    path('levels/<uuid:lvl_id>/delete/', delete_level, name='delete_level'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]