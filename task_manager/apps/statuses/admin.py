from django.contrib import admin

from task_manager.apps.statuses.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
