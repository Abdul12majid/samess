from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('create_message', views.create_message, name='create_message'),
    path('get_messages', views.get_messages, name='get_messages'),
    path('get_message/<str:pk>', views.get_message, name='get_messages'),
    path('status_seen/<str:pk>', views.status_seen, name='status_seen'),

]
