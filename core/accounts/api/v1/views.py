from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
from django.contrib.auth import get_user_model
from accounts.models import Profile
from .serializer import RegistrationSerializer,AbtivationResendSerializer,ChangePasswordSerializer,ProfileSerializer,CustomAuthTokenSerializer,CustomTokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from ..utils import EmailThread
import jwt
from django.conf import settings

User= get_user_model()

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer


    def post(self,request,*args,**kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email=serializer.validated_data['email']
            data={
                'email':email
            }
           
            user_obj = get_object_or_404(User,email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation.tpl', {'token':token}, 'budeikin52@gmail.com', to=[email])
            EmailThread(email_obj).start()
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class AccountActivationView(APIView):
    def get(self,request,token,*args,**kwargs):
        try:
            token = jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'detail':'token has been expired'})
        except InvalidSignatureError:
            return Response('token is not valid')
        
        user = User.objects.get(pk=user_id)
        user.is_verified = True
        if user.is_verified:
            return Response('your account has already been verified')
        user.save()
        return Response({'detail':'this account has been verified successfully'})
        

class ActivationResendView(generics.GenericAPIView):
    serializer_class = AbtivationResendSerializer

    def post(self,request,*args,**kwargs):
        serilizer=self.serializer_class(data=request.data)
        serilizer.is_valid(raise_exception=True)
        user = serilizer.validated_data['user']
        token = self.get_tokens_for_user(user)
        email_obj = EmailMessage('email/activation.tpl', {'token':token}, 'budeikin52@gmail.com', to=[user.email])
        EmailThread(email_obj).start()
        return Response('user activation resend successfully',status=status.HTTP_201_CREATED)
      
       
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomDiscardAuthToken(APIView):
    permission_classes =[IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.GenericAPIView ):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
             # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'password changed successfully'},status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj     
