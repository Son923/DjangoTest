from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from account.models import User
from membership.badges.registry import badges

@receiver(post_save, sender=User)
def ping(sender, instance, **kwargs):
    print("PING")
    badges.possibly_award_badge("points_awarded", user=instance)
    # print(instance.meta['Membership']['Point']['point'])