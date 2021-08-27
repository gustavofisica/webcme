from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import URLValidator
from PIL import Image

def nomear_pasta(instancia, arquivo):
    """Retorna a string de uma pasta para a galeria de imagens do usuário"""
    return f'{instancia.caminho_armazenamento}/{arquivo}'

class Usuario(AbstractUser):
    """Usuário personalizado para o projeto CME"""
    foto_de_perfil = models.ImageField(upload_to=nomear_pasta, blank=True)
    caminho_armazenamento = models.UUIDField(default=uuid.uuid4, editable=False)
    curriculo_lattes = models.URLField(blank=True, validators=[URLValidator(schemes='http://lattes.cnpq.br/')])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.foto_de_perfil:
            img = Image.open(self.foto_de_perfil.path)

            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.foto_de_perfil.path)