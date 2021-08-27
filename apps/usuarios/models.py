from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image
import uuid

# Create your models here.
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

class Docente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=255)
    conselheiro = models.BooleanField(default=False)

@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Docente.objects.create(user=instance)

@receiver(post_save, sender=Usuario)
def save_user_profile(sender, instance, **kwargs):
    instance.docente.save()
