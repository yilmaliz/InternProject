from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,

        style={'input_type': 'password'}
    )
    image = serializers.ImageField(
        required = False
    )
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password","image")
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        del attrs['confirm_password']
        attrs['password'] = make_password(attrs['password'])
        return attrs




