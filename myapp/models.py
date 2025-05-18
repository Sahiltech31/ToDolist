# models.py
from django.db import models



class TodoList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    add = models.CharField(max_length=225)  # Field to store the task name
    status = models.CharField(max_length=10, default='Pending')
    
    def __str__(self):
        return self.add  # String representation of the task for easy viewing
