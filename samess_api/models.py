from django.db import models

# Create your models here.

class Status(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Receiver(models.Model):
	contact = models.CharField(max_length=20)

	def __str__(self):
		return self.contact

class Sender(models.Model):
	contact = models.CharField(max_length=20)

	def __str__(self):
		return self.contact

class Message(models.Model):
	sender = models.CharField(max_length=20)
	receiver = models.CharField(max_length=20)
	iv = models.CharField(default="iv",max_length=500)
	status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)
	text = models.TextField("Message", blank=True)

	def __str__(self):
		return (f'{self.sender} {self.receiver}')
