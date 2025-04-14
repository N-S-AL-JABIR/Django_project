from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_no = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.name} - {self.roll_no}"