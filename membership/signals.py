from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from .registry import badges

from account.models import User

# @receiver(post_save, sender=User)
# def award_membership(sender, instance, **kwargs):
#     badges.possibly_award_badge("membership_awarded", user=instance)
#     print("Badge awarded !!!")



# from pinax-badges
badge_awarded = Signal(providing_args=["badge"])