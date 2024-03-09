
from django.db import models

#Create your models here


class Store(models.Model):
    store_name=models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    payment_type=models.CharField(max_length=100)

    def _str_(self):
        return self.store_name
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    def _str_(self):
        return self.name


class Product(models.Model):
    RATING_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    production_date=models.DateField()
    expiry_date=models.DateField()
    rating=models.IntegerField(choices=RATING_CHOICES)
    store=models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.product_name



    