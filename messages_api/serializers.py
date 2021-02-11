from rest_framework import serializers
from .models import CreateMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMessage
        fields = ['id', 'name', 'email', 'message']
