from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
import os, sys
import uuid



def nomear_pasta(instancia, arquivo):
    return f'{instancia.caminho_armazenamento}/{arquivo}'
# Create your models here.
class Usuario(AbstractUser):
    foto_de_perfil = models.ImageField(upload_to=nomear_pasta, blank=True)
    caminho_armazenamento = models.UUIDField(default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.foto_de_perfil:
            img = Image.open(self.foto_de_perfil.path)

            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.foto_de_perfil.path)
