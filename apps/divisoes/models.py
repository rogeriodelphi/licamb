# from django.contrib.auth.models import User
from django.db import models


class Divisao(models.Model):
    codigo = models.CharField(max_length=1, unique=True, null=False, blank=False, verbose_name='Código')
    descricao = models.CharField(max_length=80, unique=True, verbose_name='Descrição')

    class Meta:
        db_table = 'Divisao'
        ordering = ['codigo']
        verbose_name = 'Divisão'
        verbose_name_plural = 'Divisões'

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.descricao)
