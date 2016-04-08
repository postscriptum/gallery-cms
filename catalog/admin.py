from django.contrib import admin
from .models import Gallery, Image


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_images')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('galleries',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
