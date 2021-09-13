from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Externo(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    tipo_de_instituicao = models.CharField(max_length=40)
    razao_social = models.CharField(max_length=250)
    cnpj_regex = RegexValidator(
        regex=r'/^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$/', message='O ramal deve estar no seguinte formato: 00.000.000/0000-00')
    cnpj = models.CharField(validators=[cnpj_regex], max_length=20)
    cep_regex = RegexValidator(
        regex=r'[0-9]{5}-[0-9]{3}', message='O ramal deve estar no seguinte formato: 00000-000')
    cep = models.CharField(validators=[cep_regex], max_length=10)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    rua = models.CharField(max_length=250)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=250)
    telefone_instituicao_regex = RegexValidator(
        regex=r'\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}', message='O telefone de estar no formato de : (xx) xxxxx-xxxx')
    telefone_instituicao = models.CharField(
        validators=[telefone_instituicao_regex], max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.usuario.get_full_name()
