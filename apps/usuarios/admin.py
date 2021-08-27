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
        ("Informações Pessoais", {"fields": (
            "foto_de_perfil", "curriculo_lattes",
        )}),
    )

admin.site.unregister(models.Group)
