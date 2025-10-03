from django.urls import path
from .views import RegisterUserView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register-user/', RegisterUserView.as_view(), name="register-user"),
    path("token/",TokenObtainPairView.as_view(),name="token-obtain-pair"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token-refresh-view"),
]
