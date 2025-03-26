from django.apps import AppConfig


class PRofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'p_rofile'

    def ready(self):
        import p_rofile.signals 
