from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 
                  'name', 
                  'email', 
                  'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
