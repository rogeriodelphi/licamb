from django.db import models
from apps.subgrupos.models import SubGrupo
from apps.core.funcoes import potencial_poluidor

class Unidade_Medida(models.Model):
    und_medida_desc = models.CharField(max_length=255, unique=True ,verbose_name='Unidade de Medida')

    class Meta:
        db_table = 'Unidade_medida'
        ordering = ['und_medida_desc']
        verbose_name = 'Unidade de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.und_medida_desc


class Tipologia(models.Model):
    PP_CHOICES = potencial_poluidor.choices_potencial_poluidor()

    codigo = models.CharField(max_length=6, unique=True, null=False, blank=False, verbose_name='Código')
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='SubGrupo')
    descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')
    und_medida_desc = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE, verbose_name='Unidade de Medida')
    # und_medida_valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Unidade de Medida(Valor)')
    p_poluidor = models.CharField(max_length=1, choices=PP_CHOICES, verbose_name='Potencial Poluidor')


    class Meta:
        db_table = 'Tipologia'
        ordering = ['subgrupo']
        verbose_name = 'Tipologia'
        verbose_name_plural = 'Tipologias'

    def __str__(self):
        return self.subgrupo
