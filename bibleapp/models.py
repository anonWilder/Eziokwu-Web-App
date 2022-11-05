from django.db.models.deletion import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(null=False,blank=False,max_length=250)
    
    def __str__(self):
        return self.name


class subcategory(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(null=False,blank=False,max_length=250)

    def __str__(self):
        return self.name

class header(models.Model):
    subcategory = models.ForeignKey(subcategory,on_delete=models.CASCADE,null=False,blank=False)
    header = models.CharField(null=False,blank=False,max_length=250)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.subcategory) + ' '+ self.header 