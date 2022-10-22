from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.sales'
    verbose_name = "Mod. Ventas"

    def ready(self):
        import applications.sales.signals #accounts is a name of app
