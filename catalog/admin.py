from django.contrib import admin
from .models import Gallery, Image


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
