from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name  = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Our Door','Our Door')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL) 
    dateCreated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
    note = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.product.name