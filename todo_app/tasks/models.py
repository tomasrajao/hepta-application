from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=300, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    active = models.BooleanField(verbose_name='Ativo', default=True)
    modified_at = models.DateTimeField(verbose_name='Modificado em', auto_now=True)
    registered_at = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True)

    def __str__(self):
        return self.title

    def truncated_description(self):
        if len(self.description) > 30:
            return f'{self.description[:30]}...'
        return self.description

    truncated_description.short_description = 'Descrição'
