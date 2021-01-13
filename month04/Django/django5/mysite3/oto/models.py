from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField('作家', max_length=20)


class Wife(models.Model):
    name = models.CharField('妻子', max_length=20)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
