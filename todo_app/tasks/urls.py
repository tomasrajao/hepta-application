from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('list-tasks/', views.list_tasks, name='list-tasks'),
    path('add-tasks/', views.add_tasks, name='add-tasks')
]
