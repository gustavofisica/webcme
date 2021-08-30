from django.db import models
from django.conf import settings


class Docente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=255)
    conselheiro = models.BooleanField(default=False)
