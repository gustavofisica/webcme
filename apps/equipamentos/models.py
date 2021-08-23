from django.db import models

# Create your models here.
class Equipamento(models.Model):
    nome_do_equipamento = models.CharField(max_length=255)
    descricao = models.TextField()


    def __str__(self):
        return self.nome_do_equipamento