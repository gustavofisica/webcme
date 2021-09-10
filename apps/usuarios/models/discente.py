from usuarios.models import Docente
from django.db import models
from django.conf import settings


class Discente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    vinculo = models.CharField(max_length=25, blank=True, null=True)
    inicio_vinculo = models.DateField()
    setor = models.CharField(max_length=250, blank=True, null=True)
    departamento = models.CharField(max_length=250, blank=True, null=True)
    periodo_de_permanencia = models.DateField(null=True)

    def __str__(self):
        return self.usuario.get_full_name()
