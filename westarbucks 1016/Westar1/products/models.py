from django import db
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    Nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits = 6, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    saturated_fa_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    size_ml = models.DecimalField(max_digits = 6, decimal_places = 2)
    size_fluid_ounce = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergys'

class Allergy_product(models.Model):
    Allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'