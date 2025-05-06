from django.db import models
from django.utils.text import slugify
import datetime


# Create your models here.
class models_test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # auto_field = models.AutoField(primary_key=True)
    # auto_big_field = models.BigAutoField()

    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=100)
    date_field = models.DateField(default=datetime.date.today)
    date_time_field = models.DateTimeField(default=datetime.datetime.now)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to="uploads/")
    # file_path_field = models.FilePathField(path="/path/to/files/")
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField(default="127.0.0.1") 
    image_field = models.ImageField(upload_to="images/")
    json_field = models.JSONField(default=dict)
    null_boolean_field = models.BooleanField(null=True, blank=True)
    slug_field = models.SlugField(default="default-slug")
    text_field = models.TextField(default="Enter your text here...")
    time_field = models.TimeField(default=datetime.time(9, 0))
    url_field = models.URLField(default="https://example.com")
    uuid_field = models.UUIDField(default="00000000-0000-0000-0000-000000000000")
