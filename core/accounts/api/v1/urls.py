from django.urls import path,include
from .views import RegistrationApiView,CustomAuthToken,CustomDiscardAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name='api-v1'

urlpatterns = [
   path('register/',RegistrationApiView.as_view(),name='registration'),
   path('token/login/',CustomAuthToken.as_view(),name='token-login'),
   path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
   path('jwt/create/',TokenObtainPairView.as_view(),name='jwt-create'),
   path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
   path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),



]