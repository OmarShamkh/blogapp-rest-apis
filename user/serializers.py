from email import message
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    # 'write only': to ensure that the field may be used when updating or creating an instance. not in representation.
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        # check if user email exists
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")    

        #check that the username is unique
        username_exists = User.objects.filter(username=attrs["username"]).exists()
        if username_exists:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        # Store Hashed password
        user.set_password(password)
        user.save()
        # create a token for authentication
        Token.objects.create(user=user)
        # Create new user
        return user
    

class LoginSerializer(serializers.Serializer):
    """
    This serializer try to authenticate the user with when validated.
    """
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Authenticate the user using Django auth framework.
            user = authenticate(username=username, password=password)
            if not user:
                message = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(message, code='authorization')
        
        attrs['user'] = user
        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    """
    This serializer will be used to logout a user.
    """

    def validate(self, attrs):
        user = attrs.get('user')
        if user:
            attrs['user'] = user
            return attrs
        else:
            message = 'User is not logged in.'
            raise serializers.ValidationError(message, code='authorization')