# Generated by Django 3.2.7 on 2021-10-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0009_alter_tipologia_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='pdf',
            field=models.ImageField(blank=True, null=True, upload_to='tipologias', verbose_name='Comprovante'),
        ),
    ]