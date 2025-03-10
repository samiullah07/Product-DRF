from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=7)



class ProductGenric(models.Model):
    name = models.CharField(max_length=50,default=None)
    category = models.CharField(max_length=50)
    
    


