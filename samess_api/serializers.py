from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Message, Receiver, Sender


class MessageSerializer(serializers.Serializer):
	sender=serializers.CharField(max_length=500)
	receiver=serializers.CharField(max_length=500)
	text=serializers.CharField(max_length=500)
	iv=serializers.CharField(max_length=500)


class PasswordSerializer(serializers.Serializer):
	old_password=serializers.CharField()
	new_password=serializers.CharField()
	confirm_password=serializers.CharField()

class SignupSerializer(serializers.Serializer):
	first_name=serializers.CharField()
	last_name=serializers.CharField()
	username=serializers.CharField()
	password=serializers.CharField()
	email=serializers.EmailField()

class AuthSerializer(serializers.Serializer):
	auth_token=serializers.CharField()
