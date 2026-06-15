from rest_framework import serializers
from .models import Player, Level


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = Player.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ("id", "name", "json", "owner", "creation_date")
        read_only_fields = ("owner", "creation_date", "id")

class LevelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        exclude=["json", "owner"]