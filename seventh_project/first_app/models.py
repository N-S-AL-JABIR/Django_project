from django.db import models

class Student(models.Model):
    roll= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    address= models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name} - {self.roll} '