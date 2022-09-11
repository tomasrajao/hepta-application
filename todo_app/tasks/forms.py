from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(label='Título', max_length=300)
    description = forms.CharField(
        label='Descrição', widget=forms.Textarea)
