from django.db import models
from apps.grupos.models import Grupo
from apps.subgrupos.models import SubGrupo

class Unidade_Medida(models.Model):
    und_medida_desc = models.CharField(max_length=255, verbose_name='Unidade de Medida')

    class Meta:
        db_table = 'Unidade_medida'
        ordering = ['und_medida_desc']
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.und_medida_desc


class Tipologia(models.Model):
    codigo = models.CharField(max_length=6, null=False, blank=False, verbose_name='Código')
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='Código e Descrição do SubGrupo')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    und_medida_desc = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE, verbose_name='Unidade de Medida')
    # und_medida_valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Unidade de Medida(Valor)')
    p_poluidor = models.CharField(max_length=1, verbose_name='Potencial Poluidor')
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='SubGrupo')
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'Tipologia'
        ordering = ['subgrupo']
        verbose_name = 'Tipologia'
        verbose_name_plural = 'Tipologias'

    def __str__(self):
        return self.codigo
