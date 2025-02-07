from django.contrib import admin
from .models import Order, Item
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Order)
admin.site.register(Item)