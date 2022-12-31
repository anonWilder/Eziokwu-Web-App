from django.db.models.deletion import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

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


class Video(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    discription = models.TextField(max_length=100)
    # video = models.FileField(upload_to='media/video')
    video = models.URLField(max_length = 400)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Audio(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=300)
    audio = models.FileField(upload_to='media/video')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    