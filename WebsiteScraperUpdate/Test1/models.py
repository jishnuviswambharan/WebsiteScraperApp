from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length = 250)
    img=models.ImageField(upload_to='images')
    dec=models.TextField()


class team(models.Model):
    tname=models.CharField(max_length=200)
    timg=models.ImageField(upload_to='team')
    reviw=models.TextField()

    