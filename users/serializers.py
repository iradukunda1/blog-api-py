from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import UserRegistration


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=UserRegistration.objects.all())])
    email = serializers.CharField(validators=[UniqueValidator(queryset=UserRegistration.objects.all())])
    password = serializers.CharField(write_only=True)  # do not return password in response
    password_confirmation = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = UserRegistration.objects.create_user(**validated_data)
        return user

    def validate_password(self, password):
        password_confirmation = self.context.get('request').data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'Error': 'password and password confirmation do not match'})
        return password

    class Meta:
        model = UserRegistration
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password_confirmation', 'password']
