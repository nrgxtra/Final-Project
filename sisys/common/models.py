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


class Appointment:
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, validators=)
    message = models.TextField()
