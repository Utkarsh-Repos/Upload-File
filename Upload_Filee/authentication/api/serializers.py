
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class SignUpSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        username = validated_data['email']
        if username:
            validated_data['username'] = username
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate(self, data):
        email = data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email_error': 'email_already_registered'})
        return data