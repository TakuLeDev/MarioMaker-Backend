from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

    search_fields =('name', 'id')
