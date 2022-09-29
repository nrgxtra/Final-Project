from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='services', blank=True, null=True)

    def __str__(self):
        return self.name

