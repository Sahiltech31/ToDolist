from django.contrib import admin

# Register your models here.
from .models import TodoList

# Register the Task model with the admin interface
admin.site.register(TodoList)