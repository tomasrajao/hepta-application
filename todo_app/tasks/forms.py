from django import forms

from todo_app.tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Título', max_length=300)
    description = forms.CharField(
        label='Descrição', widget=forms.Textarea)

    class Meta:
        model = Task
        fields = ['title', 'description']
