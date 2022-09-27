from django.apps import AppConfig


class PopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pop'
    
    def ready(self):
        from jobs import updater
        updater.start()