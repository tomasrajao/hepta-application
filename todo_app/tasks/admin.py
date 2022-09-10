from django.contrib import admin

# Register your models here.
from todo_app.tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'truncated_description',
        'active',
        'modified_at',
        'registered_at',
    )

