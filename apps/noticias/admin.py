from django.contrib import admin
from .models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    """Parâmetros de administração de notícias"""
    list_display = ('titulo', 'slug', 'criacao','destaque', 'status')
    prepopulated_fields = {
        'slug': ('titulo',)
    }
    list_editable = ('destaque','status',)
    list_filter = ('categoria',)

admin.site.register(Noticia, NoticiaAdmin)

