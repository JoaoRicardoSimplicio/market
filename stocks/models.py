from django.db import models

# Create your models here.


class Stock(models.Model):

    code = models.CharField(unique=True, max_length=10)
    amount = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    highest_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    lowest_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    day_variation = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    month_variation = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    year_variation = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.code
