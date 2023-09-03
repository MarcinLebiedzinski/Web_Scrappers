from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    webpage = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    link = models.CharField(max_length=256)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


