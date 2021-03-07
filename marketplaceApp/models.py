from django.db import models

# Create your models here.

class Marketplaces(models.Model):
   name = models.CharField(max_length=150)
   description = models.CharField(max_length=255)
   site = models.CharField(max_length=100)
   phone = models.IntegerField()
   email = models.CharField(max_length=100)
   technical_manager = models.CharField(max_length=255)
