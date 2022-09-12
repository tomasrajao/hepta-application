from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('listar/', views.list_tasks, name='list-tasks'),
    path('adicionar/', views.add_task, name='add-task'),
    path('editar/<int:id>/', views.edit_task, name='edit-task'),
    path('deletar/<int:id>', views.delete_task, name='delete-task'),
    # path('contatos/', views.add_contact, name='add-contact'),
]
