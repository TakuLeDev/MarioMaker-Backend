from rest_framework import serializers
from .models import User, Level

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("id", "name", "email", "hash_pswrd", "creation_date")

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields = ("id", "name", "json", "owner")