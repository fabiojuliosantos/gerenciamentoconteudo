from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import Response
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

User = get_user_model()

class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        user_name = user.name
        user_email = user.email
        user_username = user.username

        subject = 'Cadastro de Usuário'
        message = f'Olá, {user_name}. Você concluiu seu cadastro com o nome de usuário ({user_username}). Utilize seu Username e sua senha salva para logar no sistema.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

        response_data ={
            'success': 'O seu cadastro foi concluído com sucesso.',
            'message': 'Você receberá um e-mail confirmando seu cadastro.'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
class LoginUser(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        user = serializer.user

        response_data = {
            'success': 'Login efetuado com sucesso.',
            'message':{
                'access_token': tokens['access'],
                'refresh_token': tokens['refresh'],
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
