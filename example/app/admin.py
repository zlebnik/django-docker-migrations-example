from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('user',)
    search_fields = ('name',)
