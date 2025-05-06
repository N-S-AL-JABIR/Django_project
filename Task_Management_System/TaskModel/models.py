from django.db import models
from TaskCategory.models import TaskCategory
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
    