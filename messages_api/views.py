from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CreateMessage
from .serializers import MessageSerializer


class MessageListView(generics.GenericAPIView):
    queryset = CreateMessage.objects.all()
    serializer_class = MessageSerializer


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = CreateMessage
    serializer_class = MessageSerializer
