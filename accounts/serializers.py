from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['email','password','password2','role']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        role = validated_data.get('role', 'EXECUTIVE')

        # Prevent public admin creation
        if role == 'ADMIN':
            role = 'EXECUTIVE'
            
        user = User.objects.create_user(
            email=validated_data['email'],
            password= validated_data['password'],
            role = role
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password= serializers.CharField()

    def validate(self, attrs):
        user = authenticate(email = attrs['email'], password= attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid Credentials !!")
        return user
