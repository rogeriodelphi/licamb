from django.db import models
from apps.grupos.models import Grupo

class SubGrupo(models.Model):
    codigo = models.CharField(max_length=6, null=False, blank=False, verbose_name='Código')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo')
    descricao = models.CharField(max_length=50)

    class Meta:
        db_table = 'Subgrupo'
        ordering = ['grupo']
        verbose_name = 'SubGrupo'
        verbose_name_plural = 'SubGrupos'

    def __str__(self):
        return '{} - {}'.format(self.grupo, self.descricao)