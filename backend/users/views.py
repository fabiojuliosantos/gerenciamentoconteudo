from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.hashers import make_password
import string, random
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

User = get_user_model()

class RegisterUserView(CreateAPIView):
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
    
class LoginUserView(TokenObtainPairView):
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

class RedefinePasswordView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({'error:' ' E-mail não encontrado no banco.'}, status=404)
        
        user_name = user.name
        user_alias = user.username
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        user.password = make_password(password)
        user.save()

        subject = 'Redefinição da senha do Sistema de Gerenciamento de Conteúdo'
        message = f'Olá, {user_name}. você solicitou a redefinição de sua senha. \nOs dados do seu login são os seguintes:\n\nUsername: {user_alias} \nSenha: {password}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        response_data = {
            'success': 'Senha redefinida',
            'message': 'A nova senha foi enviada via e-mail.'
        }

        return Response(response_data)

class UpdateUserView(APIView):

    def put(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response({"res": f"Usuário com id={user_id} não existe"}, status=status.HTTP_400_BAD_REQUEST)
        if user_instance != request.user:
            return Response({"res": "Você não tem permissão para modificar esse usuário."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data

        serializer = UserSerializer(instance=user_instance, data=data, partial=True)        

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)