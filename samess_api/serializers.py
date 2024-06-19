from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Message, Receiver, Sender


class MessageSerializer(serializers.Serializer):
	sender=serializers.CharField(max_length=500)
	receiver=serializers.CharField(max_length=500)
	text=serializers.CharField(max_length=500)
	iv=serializers.CharField(max_length=500)

class MessageSerializer2(serializers.ModelSerializer):
	seen_status = serializers.SerializerMethodField()
	def get_seen_status(self, obj):
		if obj.status.id == 1:
			return 'Unseen'
		elif obj.status.id == 2:
			return 'Seen'
		else:
			return 'unknown'
	class Meta:
		model=Message
		fields=('id', 'sender', 'receiver', 'iv', 'text', 'seen_status',)


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
