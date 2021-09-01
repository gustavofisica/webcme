from django.contrib import admin
from django.contrib.auth import admin as AuthUserAdmin, models
from django.http import request

from .forms import UsuarioFormularioCriacao, UsuarioFormularioModificacao
from .models import Usuario, Docente

@admin.register(Usuario)
class UsuarioAdmin(AuthUserAdmin.UserAdmin):
    form = UsuarioFormularioModificacao
    add_form = UsuarioFormularioCriacao
    model = Usuario
    fieldsets = AuthUserAdmin.UserAdmin.fieldsets + (
        ("Outras Informações", {"fields": (
            "foto_de_perfil", "curriculo_lattes", "celular",
        )}),
        ("Informações Institucionais", {"fields": (
            "eh_conselheiro", "eh_docente", "eh_discente", "eh_tecnico", "eh_chefe", "eh_sub_chefe", "operacao",
        )}),
    )

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
admin.site.unregister(models.Group)
