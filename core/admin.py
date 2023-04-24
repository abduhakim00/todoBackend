from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from todomain.models import Todo
from todomain.admin import TodoAdmin


# class TagInline(GenericTabularInline):
#     autocomplete_fields = ['tag']
#     model = TaggedItem


# class CustomProductAdmin(TodoAdmin):
#     inlines = [TagInline]


# admin.site.unregister(Todo)
# admin.site.register(Todo, CustomProductAdmin)


# # Register your models here.
