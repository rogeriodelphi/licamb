# Generated by Django 3.2.7 on 2021-10-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0004_alter_tipologia_p_poluidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade_medida',
            name='und_medida_desc',
            field=models.CharField(max_length=255, unique=True, verbose_name='Unidade de Medida'),
        ),
    ]
