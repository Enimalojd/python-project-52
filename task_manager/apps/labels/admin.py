from django.contrib import admin

from task_manager.apps.labels.models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
