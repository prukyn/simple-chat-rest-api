import json

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ChatUserSerializer, MessageSerializer
from .models import ChatUser, Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request, page=None):
        """
        This view should return a list of the <page> 10 messages
        ordered by create_date
        """
        page = self.kwargs['page']
        messages = Message.objects.all()[page*10:(page+1)*10]
        page = self.paginate_queryset(messages)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data) 

        serializer = self.get_serializer(page, many=True)        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = json.loads(json.dumps(request.data))
        serializer = self.serializer_class(data=data)
        print(data)
        if serializer.is_valid():
            try:
                author = ChatUser.objects.get(email=serializer.data['author']['email'])
            except ObjectDoesNotExist:
                author = ChatUser.objects.create(email=serializer.data['author']['email'])

            message = Message.objects.create(text=serializer.data['text'], author=author)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
