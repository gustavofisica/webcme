from django.db import models

# Create your models here.
class Noticia(models.Model):
    """Entidade de Notícias do Banco de Dados"""
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    texto = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    edicao = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)
    ESCOLHAS_CATEGORIA = (
        ('comunicados', 'Comunicados'),
        ('equipamentos', 'Equipamentos'),
        ('compras', 'Compras'),
        ('manutencao', 'Manutenção'),
        ('treinamentos', 'Treinamentos'),
        ('pesquisa', 'Pesquisa'),
    )
    categoria = models.CharField(max_length=15, choices=ESCOLHAS_CATEGORIA, default='comunicados')

    def __str__(self):
        return self.titulo
