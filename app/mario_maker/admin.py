from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'creation_date')

    search_fields = ('id', 'username', 'creation_date')
