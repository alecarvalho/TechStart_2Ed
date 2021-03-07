from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=255)
    description= models.CharField(max_length=255)

class Product(models.Model):
    name= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    price= models.DecimalField(decimal_places=2, max_digits=10)
    categories = models.ManyToManyField('Category', related_name='Product', blank=True)
