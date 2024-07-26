from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from app.core.models import BaseModel


class GenderOption(TextChoices):
    MASCULINO = "M", _("Masculino")
    FEMININO = "F", _("Feminino")
    NAO_INFORMAR = "N", _("Não Informar")


class Person(BaseModel):
    name = models.CharField(verbose_name="Nome", max_length=255)
    birthdate = models.DateTimeField(verbose_name="Data de Nascimento")
    cpf = models.CharField(verbose_name="CPF", max_length=12)
    gender = models.CharField(
        verbose_name="Gênero",
        max_length=12,
        choices=GenderOption.choices,
        default=GenderOption.NAO_INFORMAR
    )
    height = models.DecimalField(verbose_name="Altura", max_digits=8, decimal_places=2)
    weight = models.DecimalField(verbose_name="Peso", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.name
