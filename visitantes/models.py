from unittest.util import _MAX_LENGTH
from django.db import models

class Visitante(models.Model):

    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now_add=False,
        auto_now=False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada",
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa de veiculo",
        max_length=7,
        blank=True,
        null=True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True
    )

    horario_saida = models.DateField(
        verbose_name="Horario de saída do condomínio",
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo