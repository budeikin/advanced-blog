from django.urls import path,include
from .views import ProfileAPIView,RegistrationApiView,CustomAuthToken,CustomDiscardAuthToken,ChangePasswordAPIView,TestEmailView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

app_name='api-v1'

urlpatterns = [
   path('register/',RegistrationApiView.as_view(),name='registration'),
#    path('activation/confirm/',RegistrationApiView.as_view(),name='registration'),
   path('test-email/',TestEmailView.as_view(),name='send-email'),


   path('change-password/',ChangePasswordAPIView.as_view(),name='change-password'),
   path('token/login/',CustomAuthToken.as_view(),name='token-login'),
   path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
#    path('jwt/create/',CustomTokenObtainPairView.as_view(),name='jwt-create'),
#    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
#    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
   path('profile/',ProfileAPIView.as_view(),name='profile')
]