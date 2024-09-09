from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views import SignupAPIView, LogoutView, ProfileAPIView, DeleteAPIView

urlpatterns = [
    path("", SignupAPIView.as_view(), name='signup'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/", DeleteAPIView.as_view(), name="user_delete"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", ProfileAPIView.as_view(), name="user_profile"),
]