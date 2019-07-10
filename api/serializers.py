from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import ChatUser, Message


class ChatUserSerializer(serializers.Serializer):
    email = serializers.EmailField()



class MessageSerializer(serializers.Serializer):    
    text = serializers.CharField(max_length=100)
    author = ChatUserSerializer()
    create_date = serializers.DateTimeField(required=False)