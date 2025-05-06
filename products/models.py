from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name