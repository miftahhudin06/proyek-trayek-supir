from django.apps import AppConfig


class AdministratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'administrator'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import administrator.signals  # noqa
