from django.db import models
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
import os.path


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.SmallIntegerField(default=10)
    enabled = models.BooleanField(default=True)

    def number_of_images(self):
        return self.image_set.count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Galleries"


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    galleries = models.ManyToManyField(Gallery, blank=True)

    def preview_url(self):
        img_path, img_file = os.path.split(self.file.url)
        return os.path.join(img_path, 'previews', 'thumb_' + img_file)

    def list_display_preview(self):
        return format_html('<img src="{}" height="150">', self.preview_url())
    list_display_preview.allow_tags = True
    list_display_preview.short_description = 'Image'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = RichTextUploadingField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
