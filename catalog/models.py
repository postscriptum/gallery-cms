from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def number_of_images(self):
        return self.image_set.count()

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    galleries = models.ManyToManyField(Gallery, blank=True)

    def __str__(self):
        return self.name
