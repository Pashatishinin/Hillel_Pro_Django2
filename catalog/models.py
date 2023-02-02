from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField("name", max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("name", max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Client(models.Model):
    name = models.CharField("name", max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField("name", max_length=30)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



