from django.contrib import admin

from task_manager.apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "executor", "created_at")
    list_filter = ("status", "executor")
    search_fields = ("name", "description")
    ordering = ("created_at",)