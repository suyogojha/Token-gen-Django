from rest_framework import serializers
from home.models import *
from django.contrib.auth.models import User


class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
    def create(self , validated_date):
        user = User.objects.create(username = validated_date['username'])
        user.set_password(validated_date['password'])
        user.save()
        return user