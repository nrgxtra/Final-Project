from django.db import models

from sisys.blog_app.models import Category, Tags


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    picture = models.ImageField(upload_to='services_pics')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
