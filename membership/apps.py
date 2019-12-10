from django.apps import AppConfig
from django.db.models.signals import post_save

class MembershipConfig(AppConfig):
    name = 'membership'

    def ready(self):
        import membership.signals
