from django.apps import AppConfig


class StoreAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Store_App'

def ready(self):
    from . import signal
