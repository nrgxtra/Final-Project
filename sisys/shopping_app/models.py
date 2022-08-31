
from django.conf import settings
from django.db import models

from sisys.sisis_auth.models import SisisUser


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name
