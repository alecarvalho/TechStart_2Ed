from django.db import models

# Create your models here.

class Sellers(models.Model):
    trade_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
