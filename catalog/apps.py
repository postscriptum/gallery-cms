from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from catalog.signals import make_preview, delete_images


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        image_model = self.get_model('Image')
        # after image saving call 'make_preview' to make image preview
        post_save.connect(make_preview, sender=image_model)
        # after image deleting call 'delete_images' to delete unused image files
        post_delete.connect(delete_images, sender=image_model)
