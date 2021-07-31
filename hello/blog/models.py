from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class BlogVisiter(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Hobby(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    explain = models.TextField()

    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    explain = models.TextField()

    def __str__(self):
        return self.title

class Pictures(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    explain = models.TextField()

    def __str__(self):
        return self.title

class Place(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    explain = models.TextField()

    def __str__(self):
        return self.title