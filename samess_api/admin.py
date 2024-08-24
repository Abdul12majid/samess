from django.contrib import admin
from .models import Message, Receiver, Sender, Status

# Register your models here.

admin.site.register(Receiver)
admin.site.register(Sender)
admin.site.register(Status)


@admin.register(Message)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('sender', 'receiver',)
	ordering = ('-id',)
	search_fields = ('text',)