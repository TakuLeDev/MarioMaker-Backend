from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class Player(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    #follows = models.ManyToManyField("self", related_name="user_follows", null=True)

    creation_date = models.DateField(auto_now_add=True, auto_now=False)

class Level(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

        name = models.CharField(max_length=255, null=False, default="3")
        json = models.JSONField()
        owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

