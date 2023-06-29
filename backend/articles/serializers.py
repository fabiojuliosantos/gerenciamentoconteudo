from rest_framework import serializers
from .models import Article, Category, Tag

class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id',
                  'title', 
                  'text', 
                  'created_at', 
                  'updated_at', 
                  'liked_by', 
                  'tags', 
                  'user',
                  'user_name']
    
    def get_user_name(self,obj):
        user = obj.user
        return user.name if user else None