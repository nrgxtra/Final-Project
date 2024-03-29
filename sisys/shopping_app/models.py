from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.email


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    picture = models.ImageField(blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def pictureURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_quantity(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if not item.product.digital:
                shipping = True
        return shipping

    @property
    def order_items(self):
        orderitems = [str.join('-', [item.product.name, str(item.quantity)]) for item in self.orderitem_set.all()]
        return orderitems

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    province = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=150, null=False)
    post_code = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
