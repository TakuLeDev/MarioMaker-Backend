from rest_framework import serializers
from .models import Player, Level

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields = ("id", "name", "email", "creation_date")

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields = ("id", "name", "json", "owner")