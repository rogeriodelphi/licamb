from django.db import models
from apps.divisoes.models import Divisao

class Grupo(models.Model):
    codigo = models.CharField(max_length=3, null=False, blank=False, verbose_name='Código')
    divisao = models.ForeignKey(Divisao, on_delete=models.CASCADE, verbose_name='Divisão')
    descricao = models.CharField(max_length=110)

    class Meta:
        db_table = 'Grupo'
        ordering = ['divisao']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return '{}-{}-{}'.format(self.codigo, self.divisao, self.descricao)
