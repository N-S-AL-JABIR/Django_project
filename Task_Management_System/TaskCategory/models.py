from django.db import models


class TaskCategory(models.Model):
    task_name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.task_name