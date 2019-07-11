import re
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import ChatUser, Message


class ChatUserSerializer(serializers.Serializer):
    '''
    Serializer that represent chatuser
    using CharField, because must validate email field by regex
    '''
    email = serializers.RegexField(r'^[^@]+@[^@]+\.[^@]+$')


class MessageSerializer(serializers.Serializer):
    text = serializers.RegexField(r'[\w|\W]{1,100}')
    create_date = serializers.DateTimeField(read_only=True)
    author = ChatUserSerializer()

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        user = ChatUser.objects.get_or_create(email=author_data['email'])[0]
        message = Message.objects.create(author=user, **validated_data)
        return message