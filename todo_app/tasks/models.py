from django.db import models
from django.urls import reverse


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    active = models.BooleanField(verbose_name='Ativo', default=True)
    modified_at = models.DateTimeField(verbose_name='Modificado em', auto_now=True)
    registered_at = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='Contato')

    class Meta:
        ordering = ['-active', '-modified_at', '-registered_at', ]
        verbose_name = 'Tarefa'

    def __str__(self):
        return self.title

    def truncated_description(self):
        if len(self.description) > 33:
            return f'{self.description[:30]}...'
        return self.description

    truncated_description.short_description = 'Descrição'


class Contact(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=200)
    email = models.EmailField(verbose_name='Email', max_length=254)
    modified_at = models.DateTimeField(verbose_name='Modificado em', auto_now=True)
    registered_at = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'

    def __str__(self):
        return self.name
