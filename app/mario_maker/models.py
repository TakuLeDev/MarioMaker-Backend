from django.db import models
from django.conf import settings
from uuid import uuid4

# Create your models here.
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.user.username
    
