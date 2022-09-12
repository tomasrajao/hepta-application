from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('list/', views.list_tasks, name='list-tasks'),
    path('add/', views.add_task, name='add-task'),
    path('edit/<int:id>/', views.edit_task, name='edit-task'),
]
