from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Docente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    instituicional = models.JSONField(default=dict)
    ramal_regex = RegexValidator(
        regex=r'[0-9]{4}', message='O ramal de estar no formato de : 0000')
    ramal = models.CharField(
        validators=[ramal_regex], max_length=4, null=True, blank=True)
