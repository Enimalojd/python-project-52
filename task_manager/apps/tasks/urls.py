from django.urls import path

from task_manager.apps.tasks import views


urlpatterns = [
    path("", views.Index.as_view(), name="tasks"),
    path("create/", views.TaskCreateView.as_view(), name="create_task"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="update_task"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete_task"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="current_task"),
]
