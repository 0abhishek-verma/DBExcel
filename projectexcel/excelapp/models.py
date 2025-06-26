from django.db import models

# Create your models here.
class Product(models.Model):
    Productname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    HSN = models.CharField(max_length=20, unique=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.Productname
    