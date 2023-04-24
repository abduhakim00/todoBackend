from django.contrib import admin
from . import models


# class TagInline(admin.TabularInline):
#     model = models.Tag
# Register your models here.
@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'priority']
    list_per_page = 10
    # inlines=[TagInline]



# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    list_per_page = 10
    search_fields = ['name']


