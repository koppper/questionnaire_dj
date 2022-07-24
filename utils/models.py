from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name=_('utils.base_model.uuid')
    )

    class Meta:
        abstract = True
        ordering = ('uuid', )


class AbstractTimeTracker(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('utils.date_model.created_at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('utils.date_model.updated_at')
    )

    class Meta:
        abstract = True
        ordering = ('updated_at', 'created_at')
