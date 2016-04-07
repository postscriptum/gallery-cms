from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    description = models.TextField()
    galleries = models.ManyToManyField(Gallery)
