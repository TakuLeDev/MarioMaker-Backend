from django.contrib import admin
from .models import Player, Level

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'creation_date')
    search_fields = ('name', 'owner__username')
    
# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

    search_fields = ('id', 'username')

