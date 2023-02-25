from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator


class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="no_pic.jpg")

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="no_pic.jpg")

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="no_pic.jpg")
    registered_at = models.DateField(default=date.today)

    def __str__(self):
        return self.user.username


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="no_pic.jpg")
    registered_at = models.DateField(default=date.today)

    def __str__(self):
        return self.user.username


class Store(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(StoreOwner, on_delete=models.PROTECT)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(default="no_pic.jpg")
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT)
    price = models.FloatField(validators=[MinValueValidator(1.)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    info = models.TextField(blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def display_items(self):
        return list(self.items.all())

    @property
    def total_price(self):
        tot_price = 0
        for i in Item.objects.filter(mybag__id=self.id):
            tot_price += i.price
        return tot_price


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateField(default=date.today)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def display_items(self):
        return list(self.items.all())

    @property
    def total_price(self):
        tot_price = 0
        for i in Item.objects.filter(purchase__id=self.id):
            tot_price += i.price
        return tot_price
