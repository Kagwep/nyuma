from distutils.command.upload import upload
from pyexpat import model
from sre_constants import MAX_UNTIL
from django.db import models

# Create your models here.

class Category(models.Model):
    cat =(("Rent","Rent"),
          ("Buy","Buy")
    )
    catname = models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return self.catname
    

class SubCategories(models.Model):
    SubCat = (
        ("Houses","Houses"),
        ("Apartments","Apartments"),
        ("Commercial Property","Commercial Property"),
        ("3-Bedroom","3-Bedroom"),
        ("2-Bedroom","2-Bedroom"),
        ("1-Bedroom","1-Bedroom"),
        ("Bedsitter","Bedsitter"),   
              
    )

    name = models.CharField(max_length=200,choices=SubCat)

    def __str__(self):
        return self.name

class SubCategoriesCars(models.Model):
    SubCat = (
        ("SUV.","SUV"),
        ("Hatchback","Hatchback"),
        ("Crossover","Crossover"),
        ("Sedan","Sedan"),
        ("Sports Car","Sports Car"),
        ("Coupe","Coupe"),
        ("Minivan","Minivan"),   
              
    )

    name = models.CharField(max_length=200,choices=SubCat)

    def __str__(self):
        return self.name

class Property(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images/%y')
    description = models.TextField()
    location = models.CharField(max_length=200)
    price= models.FloatField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = False, blank= False)
    sub_category = models.ForeignKey(SubCategories, on_delete = models.CASCADE, null = False, blank= False)


    def __str__(self):
        return self.name
    

class Cars(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images/%y')
    description = models.TextField()
    location = models.CharField(max_length=200)
    price= models.FloatField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = False, blank= False)
    sub_category = models.ForeignKey(SubCategoriesCars, on_delete = models.CASCADE, null = False, blank= False)


    def __str__(self):
        return self.name
    
    