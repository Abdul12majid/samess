from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer, MessageSerializer2
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .models import Message, Status
from django.conf import settings


@api_view(['GET'])
def home(request):
	return Response(f'Hey stranger')


@api_view(['POST', 'GET'])
def create_message(request):

	default = Status.objects.get(id=1)
	serializer = MessageSerializer(data=request.data)
	if serializer.is_valid():
		receiver = request.data['receiver']
		sender = request.data['sender']
		iv = request.data['iv']
		text = request.data['text']
		message = Message.objects.create(
				receiver=receiver,
				sender=sender,
				text=text,
				status=default,
				iv=iv,
			)
		message.save()
		return Response({
			'user':serializer.data, 
			'detail':'message created'})
	else:
		return Response({'Info':'incorrect parameters'})

@api_view(['GET'])
def get_messages(request):
	print(settings.PASSWORD)
	messages=Message.objects.all()
	serializer=MessageSerializer2(messages, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def get_message(request, pk):
	default = Status.objects.get(id=1)
	default2 = Status.objects.get(id=2)
	#print(request.url)
	message=Message.objects.filter(receiver=pk, status=default)
	for i in message:
		i.status = default2
		i.save()
	serializer=MessageSerializer2(message, many=True)
	return Response(serializer.data)
	
@api_view(['POST', 'GET'])
def status_seen(request, pk):
	default2 = Status.objects.get(id=2)
	message = get_object_or_404(Message, id=pk)
	message.status = default2
	message.save()
	serializer=MessageSerializer2(message, many=False)
	return Response(serializer.data, status=200)


