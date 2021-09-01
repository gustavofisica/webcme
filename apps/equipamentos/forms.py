from django import forms
from django.forms import fields
from equipamentos.models import Equipamento, GeleriaEquipamento


class FormularioEquipamento(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = '__all__'


class FormularioGeleriaEquipamento(forms.ModelForm):

    class Meta:
        model = GeleriaEquipamento
        fields = '__all__'
