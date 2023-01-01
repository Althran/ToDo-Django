from django.contrib import admin
from .models import TaskTodo


@admin.register(TaskTodo)
class AdminTask(admin.ModelAdmin):
    readonly_fields = ('id', )
    date_hierarchy = 'date_created'
