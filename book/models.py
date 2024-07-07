from django.db import models
from .helpers import Save


class Author(models.Model):
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=Save.save_image_path, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Save.save_image, null=True)
    yozuvi = models.CharField(max_length=100)
    tili = models.CharField(max_length=200)
    yili = models.IntegerField()
    betlar = models.IntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

