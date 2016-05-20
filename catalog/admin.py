from django.contrib import admin
from django.db import models
from .models import Gallery, Image, Article
from common.widgets import ImageWidget


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_images', 'enabled')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    filter_horizontal = ('galleries',)
    formfield_overrides = {
        models.ImageField: {'widget': ImageWidget},
    }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
