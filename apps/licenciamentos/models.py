from django.db import models

class DocumentacaoLicenciamento(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Requerente')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    email = models.EmailField(verbose_name='E-mail')
    status = models.CharField(max_length=20, verbose_name='Status', default='Enviado')
    arquivo = models.FileField(upload_to='arquivo', verbose_name='Arquivo')

    class Meta:
        db_table = 'DocumentacaoLicenciamento'
        ordering = ['nome']
        verbose_name = 'Documentação do Licenciamento'
        verbose_name_plural = 'Documentações do Licenciamento'

    def __str__(self):
        return self.nome
