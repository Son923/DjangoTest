from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

badge_awarded = Signal(providing_args=["badge"])
