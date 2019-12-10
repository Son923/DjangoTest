from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import F, Max, Q
from core.utils.json_serializer import CustomJsonEncoder


# Create your models here.
class ModelWithMetadata(models.Model):
    private_meta = JSONField(
        blank=True, null=True, default=dict, encoder=CustomJsonEncoder
    )
    meta = JSONField(blank=True, null=True, default=dict, encoder=CustomJsonEncoder)

    class Meta:
        abstract = True

    def get_private_meta(self, namespace: str, client: str) -> dict:
        return self.private_meta.get(namespace, {}).get(client, {})

    def store_private_meta(self, namespace: str, client: str, item: dict):
        if namespace not in self.private_meta:
            self.private_meta[namespace] = {}
        self.private_meta[namespace][str(client)] = item

    def clear_stored_private_meta_for_client(self, namespace: str, client: str):
        self.private_meta.get(namespace, {}).pop(client, None)

    def get_meta(self, namespace: str, client: str) -> dict:
        return self.meta.get(namespace, {}).get(client, {})

    def store_meta(self, namespace: str, client: str, item: dict):
        if namespace not in self.meta:
            self.meta[namespace] = {}
        self.meta[namespace][str(client)] = item

    def clear_stored_meta_for_client(self, namespace: str, client: str):
        self.meta.get(namespace, {}).pop(client, None)
