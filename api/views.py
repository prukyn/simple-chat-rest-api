import json

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import MessageSerializer
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
        messages = Message.objects.order_by('-create_date')[page*10:(page+1)*10]

        if messages:
            serializer = self.get_serializer(messages, many=True)
            return Response(serializer.data)

        serializer = self.get_serializer(messages, many=True)
        return Response(data={'errors': 'There is nothing'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
