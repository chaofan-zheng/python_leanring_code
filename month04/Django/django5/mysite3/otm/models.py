from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField("出版社", max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField("书名", max_length=20)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.publisher}"
