from django.urls import path
from task_manager.apps.users import views

urlpatterns = [
    path('', views.Index.as_view(), name="users"),
    path('login/', views.Login.as_view(), name='login'), 
]