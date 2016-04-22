from django.apps import AppConfig
from django.db.models.signals import post_save
from catalog.signals import make_preview
from catalog.models import Image


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        # after image saving call 'make_preview' to make image preview
        post_save.connect(make_preview, sender=Image)
