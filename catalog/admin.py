from django.contrib import admin
from django.db import models
from .models import Gallery, Image
from common.widgets import ImageWidget


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_images')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('galleries',)
    formfield_overrides = {
        models.ImageField: {'widget': ImageWidget},
    }


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
