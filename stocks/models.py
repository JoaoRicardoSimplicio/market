import uuid

from django.db import models

# Create your models here.


class Stock(models.Model):

    code = models.CharField(unique=True, max_length=10)
    amount = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.code


class StockBuy(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='buys')
    amount = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True)


class StockSale(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='sales')
    amount = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True)