from django.db import models

from blog_app.models import Tag


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    picture = models.ImageField(upload_to='services_pics')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
