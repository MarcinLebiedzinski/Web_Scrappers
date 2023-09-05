from django.db import models

# Create your models here.


class Market(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    webpage = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.name


