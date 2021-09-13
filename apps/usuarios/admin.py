from django.contrib import admin
from django.contrib.auth import admin as AuthUserAdmin, models

from .forms import UsuarioFormularioCriacao, UsuarioFormularioModificacao
from .models import Usuario, Docente, Discente, Externo


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
            "eh_conselheiro", "eh_docente", "eh_discente", "eh_tecnico", "eh_chefe", "eh_sub_chefe", "eh_externo", "operacao",
        )}),
    )
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('first_name', 'email',)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)


@admin.register(Discente)
class DiscenteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(Externo)
class ExternoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)


admin.site.unregister(models.Group)
