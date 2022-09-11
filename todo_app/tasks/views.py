from django.shortcuts import render, redirect

from todo_app.tasks.forms import TaskForm
from todo_app.tasks.models import Task


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', context={'tasks': tasks})


def add_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})
