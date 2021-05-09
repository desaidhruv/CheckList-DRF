from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterAPIView, LogoutAPIView

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

    path('api/register/', RegisterAPIView.as_view(), name='register_view'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout_view'),
]
