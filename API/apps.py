from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'


# Setting for allowing the signals file to be read and used
class UsersConfig(AppConfig):
    name = 'API'

    def ready(self):
        import API.signals
