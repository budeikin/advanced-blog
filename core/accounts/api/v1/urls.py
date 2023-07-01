from django.urls import path,include
from .views import ProfileAPIView,RegistrationApiView,ActivationResendView,CustomAuthToken,CustomDiscardAuthToken,ChangePasswordAPIView,CustomTokenObtainPairView,AccountActivationView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

app_name='api-v1'

urlpatterns = [
      # register accounts
   path('register/',RegistrationApiView.as_view(),name='registration'),
      # activate accounts
   path('activation/confirm/<str:token>',AccountActivationView.as_view(),name='activation'),
   path('activation/resend/',ActivationResendView.as_view(),name='resend-activation'),
      # change password 
   path('change-password/',ChangePasswordAPIView.as_view(),name='change-password'),
      # auth token
   path('token/login/',CustomAuthToken.as_view(),name='token-login'),
   path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
      # jwt
   path('jwt/create/',CustomTokenObtainPairView.as_view(),name='jwt-create'),
   path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
   path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
      # profile
   path('profile/',ProfileAPIView.as_view(),name='profile')
]