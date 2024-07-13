from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class UserBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)


class NeedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def sxet_total_price(instance, obj):
        obj.total_price = obj.book.price * obj.count






