from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        print("TEST: Catalog App is Ready!!!")  #test
