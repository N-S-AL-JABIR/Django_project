from django.db import models
from Musician.models import Musician
from datetime import date

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, default=None)
    release_date = models.DateField(default=date.today)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.album_name + ' by ' + str(self.musician)
