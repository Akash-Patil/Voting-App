from django.contrib import admin

# Register your models here.

from .models import Member


@admin.register(Member)
class Memberadmin(admin.ModelAdmin): # class that inherists from admin.ModelAdmin 
    list_display = ('Name', 'Email')


