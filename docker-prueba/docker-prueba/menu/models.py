from django.db import models

# Create your models here.
class comidas(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    price = models.CharField(max_length=10)