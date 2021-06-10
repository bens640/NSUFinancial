from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'


class UsersConfig(AppConfig):
    name = 'API'

    def ready(self):
        import API.signals
