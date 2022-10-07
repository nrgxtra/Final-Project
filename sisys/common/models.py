from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    price = models.FloatField()
    image = models.ImageField(upload_to='services', blank=True, null=True)
    pic1 = models.ImageField(upload_to='services', blank=True, null=True)
    pic2 = models.ImageField(upload_to='services', blank=True, null=True)

    category = models.ManyToManyField(Category)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def pic1URL(self):
        try:
            url = self.pic1.url
        except:
            url = ''
        return url

    @property
    def pic2URL(self):
        try:
            url = self.pic2.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=12,
    )
    date = models.DateField(blank=True, null=True)
    message = models.TextField(blank=True)


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=12,
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()


class GalleryPicks(models.Model):
    image = models.ImageField(upload_to='gallery')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return f'image {self.id}'
