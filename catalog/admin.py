from django.contrib import admin
from django.db import models
from django.core import urlresolvers
from django.utils.html import format_html
from catalog.models import Gallery, Image, Article
from common.widgets import ImageWidget


class ImageInline(admin.TabularInline):
    model = Image.galleries.through
    model.__str__ = lambda x: ''
    extra = 0
    can_delete = False
    verbose_name = 'Image'
    verbose_name_plural = 'Images'
    exclude = ('image',)
    readonly_fields = ('image_preview', 'image_name', 'image_description')

    def image_preview(self, instance):
        return format_html('<a href="{}"><img src="{}" height="150"></a>',
            urlresolvers.reverse('admin:catalog_image_change', args=(instance.image.id,)),
            instance.image.preview_url())
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'

    def image_name(self, instance):
        return instance.image.name
    image_name.short_description = 'Name'

    def image_description(self, instance):
        return instance.image.description
    image_description.short_description = 'Description'

    def has_add_permission(self, request):
        return False


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_images', 'enabled')
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ('list_display_preview', 'name', 'description')
    filter_horizontal = ('galleries',)
    formfield_overrides = {
        models.ImageField: {'widget': ImageWidget},
    }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'enabled')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
