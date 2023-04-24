from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']