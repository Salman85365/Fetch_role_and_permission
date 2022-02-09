from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()
# from django.contrib.auth.models import User

from rest_framework import serializers

"""A serializer for login with username and password"""
class AuthUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=80)
    password = serializers.CharField(required=True,max_length=80,trim_whitespace=True)


# User Serializer
"""A serializer for serializing two fields of User Model. (username and email)"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
"""This serializer is used for Registering user through api/register"""
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user