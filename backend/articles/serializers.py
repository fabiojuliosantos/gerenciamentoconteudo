from rest_framework import serializers
from .models import Article, Category, Tag
from users.models import User

class ArticleSerializer(serializers.ModelSerializer):
   
    id = serializers.ReadOnlyField()
    user_name = serializers.SerializerMethodField()
    #tags = serializers.ListField(child=serializers.CharField(), required=False)
    liked_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['id',
                  'title',
                  'text',
                  'created_at',
                  'updated_at',
                  'liked_by',
                  'user',
                  'user_name']

    def get_user_name(self, obj):
        user = obj.user
        return user.name if user else None

    def create(self, validated_data):
        #tags_data = validated_data.pop('tags', [])  # Remove as tags do validated_data

        article = Article.objects.create(**validated_data)

        return article
