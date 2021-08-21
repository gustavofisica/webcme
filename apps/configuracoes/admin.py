from django.contrib import admin
from .models import Configuracoes

# Register your models here.
class ConfiguracoesAdmin(admin.ModelAdmin):
    """Parâmetros de administração de configurações"""
    list_display = ('noticias_index',)
    list_display_links = ('noticias_index',)

admin.site.register(Configuracoes, ConfiguracoesAdmin)
