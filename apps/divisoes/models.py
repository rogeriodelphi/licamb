from django.contrib.auth.models import User
from django.db import models

class Divisao(models.Model):
    codigo = models.CharField(max_length=1, null=False, blank=False, verbose_name='Código')
    descricao = models.CharField(max_length=80)

    class Meta:
        db_table = 'Divisao'
        ordering = ['codigo']
        verbose_name = 'Divisão'
        verbose_name_plural = 'Divisões'

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.descricao)