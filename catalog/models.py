from django.db import models
import os.path


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)

    def number_of_images(self):
        return self.image_set.count()

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    galleries = models.ManyToManyField(Gallery, blank=True)

    def preview_url(self):
        img_path, img_file = os.path.split(self.file.url)
        return os.path.join(img_path, 'previews', 'thumb_' + img_file)

    def __str__(self):
        return self.name
