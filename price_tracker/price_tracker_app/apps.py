from django.apps import AppConfig
from django.conf import settings


class PriceTrackerAppConfig(AppConfig):
    name = 'price_tracker_app'

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
