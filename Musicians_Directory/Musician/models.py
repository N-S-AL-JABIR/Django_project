from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    # def get_full_name(self):
    #     return self.first_name + ' ' + self.last_name
