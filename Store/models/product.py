from distutils.command.upload import upload
from statistics import mode
from unicodedata import category
from django.db import models
from .catagory import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    discription = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products/')


