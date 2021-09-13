from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import RegexValidator, URLValidator
from PIL import Image


def nomear_pasta(instancia, arquivo):
    """Retorna a string de uma pasta para a galeria de imagens do usuário"""
    return f'{instancia.caminho_armazenamento}/{arquivo}'


class Usuario(AbstractUser):
    """Usuário personalizado para o projeto CME"""
    foto_de_perfil = models.ImageField(upload_to=nomear_pasta, blank=True)
    caminho_armazenamento = models.UUIDField(
        default=uuid.uuid4(), editable=False)
    curriculo_lattes = models.URLField(blank=True, validators=[
                                       URLValidator(schemes='http://lattes.cnpq.br/')])
    celular_regex = RegexValidator(
        regex=r'\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}', message='O telefone de estar no formato de : (xx) xxxxx-xxxx')
    celular = models.CharField(
        validators=[celular_regex], max_length=15, null=True, blank=True)
    eh_conselheiro = models.BooleanField(default=False)
    eh_docente = models.BooleanField(default=False)
    eh_discente = models.BooleanField(default=False)
    eh_tecnico = models.BooleanField(default=False)
    eh_chefe = models.BooleanField(default=False)
    eh_sub_chefe = models.BooleanField(default=False)
    eh_externo = models.BooleanField(default=False)
    operacao = models.JSONField(default=dict, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.foto_de_perfil:
            img = Image.open(self.foto_de_perfil.path)

            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.foto_de_perfil.path)
    
    def __str__(self):
        return self.get_full_name()
