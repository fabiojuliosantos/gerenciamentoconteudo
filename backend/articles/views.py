from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import ArticleSerializer

# Create your views here.

class ArticleView(CreateAPIView):
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        data = {
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'tags': request.data.get('tags'),
            'user': user_id
        }

        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)