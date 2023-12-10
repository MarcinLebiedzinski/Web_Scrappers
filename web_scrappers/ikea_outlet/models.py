from django.db import models

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

class Person(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Search(models.Model):
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
 