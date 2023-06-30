from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class ArticleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        data = {
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'user': user_id
        }

        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)