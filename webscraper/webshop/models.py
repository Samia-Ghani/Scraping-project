from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=300)
    prod_category = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_image = models.ImageField()

    def __str__(self):
        return self.prod_name


