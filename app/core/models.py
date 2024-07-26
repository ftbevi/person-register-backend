import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name="Indentificador",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
