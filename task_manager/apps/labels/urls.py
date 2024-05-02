from django.urls import path
from task_manager.apps.labels import views


urlpatterns = [
    path("", views.Index.as_view(), name="users"),
    path("create/", views.LabelCreateView.as_view(), name="create_label"),
    path("<int:pk>/update/", views.LabelUpdateView.as_view(), name="update_label"),
    path("<int:pk>/delete/", views.LabelDeleteView.as_view(), name="delete_label"),
]
