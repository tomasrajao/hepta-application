from django.shortcuts import render

from todo_app.tasks.models import Task


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', context={'tasks': tasks})
