from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.files import ImageField 

# Create your models here.

class Shop(models.Model):
    image = models.ImageField(upload_to= 'cakeimage/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = RichTextField()

    def __str__(self):
        return self.name

class Decoration(models.Model):
    image = models.ImageField(upload_to= 'decorationimage/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = RichTextField()

    def __str__(self):
        return self.name

# class Cake(models.Model):
#     image = models.ImageField(upload_to= 'cakeimage/')
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class Cupcake(models.Model):
#     image = models.ImageField(upload_to= 'cakeimage/')
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class Weddingcake(models.Model):
#     image = models.ImageField(upload_to= 'cakeimage/')
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.name

# class Brownie(models.Model):
#     image = models.ImageField(upload_to= 'cakeimage/')
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.firstName




class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class SubSubCategory(models.Model):
    category2 = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField(max_length=30)
    description = RichTextField()

    def __str__(self):
        return self.name


