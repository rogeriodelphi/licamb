from django.db import models
from apps.grupos.models import Grupo


class SubGrupo(models.Model):
    codigo = models.CharField(max_length=7, unique=True, null=False, blank=False, verbose_name='Código')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo')
    descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')

    class Meta:
        db_table = 'Subgrupo'
        ordering = ['grupo']
        verbose_name = 'SubGrupo'
        verbose_name_plural = 'SubGrupos'

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.descricao)
