from django.shortcuts import render, redirect, get_object_or_404, reverse

from todo_app.tasks.forms import TaskForm
from todo_app.tasks.models import Task


def list_tasks(request):
    try:
        a = request.session['title']
        request.session['title'] = ''
    except KeyError:
        a = ''
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', context={'tasks': tasks, 'a': a})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:list-tasks'))
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list-tasks')
    else:
        form = TaskForm(initial={'title': task.title, 'description': task.description, 'contact': task.contact, 'active': task.active})

    return render(request, 'tasks/edit_task.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    request.session['title'] = {'deleted': task.title}
    return redirect(reverse('tasks:list-tasks'))
