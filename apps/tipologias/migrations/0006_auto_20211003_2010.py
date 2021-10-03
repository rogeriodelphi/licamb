# Generated by Django 3.2.7 on 2021-10-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0005_alter_unidade_medida_und_medida_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='codigo',
            field=models.CharField(max_length=6, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='descricao',
            field=models.CharField(max_length=100, unique=True, verbose_name='Descrição'),
        ),
    ]