from django.db import models
from apps.resolucao.models import *


# class Licenca(models.Model):
#     divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE, verbose_name='Divisão')
#     grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo')
#     subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE, verbose_name='SubGrupo')
#     tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, verbose_name='Tipologia')
#     # und_medida_desc = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE, verbose_name='Unidade de Medida')
#
#     class Meta:
#         db_table = 'licenca'
#         ordering = ['subgrupo']
#         verbose_name = 'Licenca'
#         verbose_name_plural = 'Licencas'
#
#     def __str__(self):
#         return '{} - {}'.format(self.tipologia, self.tipologia.descricao)
