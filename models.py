from django.db import models
from django.conf import settings
from uuid import uuid4

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=20, null=False, default="1")
    hash_pswrd = models.CharField(max_length=255, null=False, default="2")

    follows = models.ManyToManyField("self",)

    def __str__(self):
        return self.name

class Level(models.Model):
        id = models.IntegerField(primary_key=True, default=uuid4, editable=False)

        name = models.CharField(max_length=255, null=False, default="3")
        json = models.JSONField()
        owner = models.ForeignKey(User, on_delete=models.CASCADE)

