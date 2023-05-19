from django.db import models


class ADS(models.Model):
    STATUS_CHOICES = [
        ("True", 'Опубликовано'),
        ("False", 'Не опубликовано')
    ]
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
    price = models.CharField(max_length=20)
    description = models.CharField(max_length=5000)
    address = models.CharField(max_length=100)
    is_published = models.CharField(max_length=5, choices=STATUS_CHOICES)


class Categories(models.Model):
    name = models.CharField(max_length=50)
