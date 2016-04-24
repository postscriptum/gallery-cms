from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from catalog.signals import make_preview, delete_images
from catalog.models import Image


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        # after image saving call 'make_preview' to make image preview
        post_save.connect(make_preview, sender=Image)
        # after image deleting call 'delete_images' to delete unused image files
        post_delete.connect(delete_images, sender=Image)
