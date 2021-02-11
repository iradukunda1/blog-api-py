from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from . import serializers


class UsersView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        context = {'request': request}
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            data = {'success': True}
            data.update(serializer.data)
            return Response(data=data
                            , status=status.HTTP_201_CREATED)
        except:
            return Response(data={'success': False, 'message': 'Please enter valid data'})
