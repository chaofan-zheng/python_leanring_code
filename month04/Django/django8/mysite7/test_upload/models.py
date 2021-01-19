from django.db import models


# Create your models here.
class Content(models.Model):
    desc = models.CharField(max_length=100)
    myfile = models.FileField(upload_to='myfiles')
