from django.db import models
from django.conf import settings
from usuarios.models.usuario import Usuario
from django.db.models.signals import post_save
from django.dispatch import receiver

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