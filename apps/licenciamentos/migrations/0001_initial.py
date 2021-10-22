# Generated by Django 3.2.7 on 2021-10-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentacaoLicenciamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Requerente')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('arquivo', models.ImageField(blank=True, null=True, upload_to='arquivo', verbose_name='Arquivo')),
            ],
            options={
                'verbose_name': 'Documentação do Licenciamento',
                'verbose_name_plural': 'Documentações do Licenciamento',
                'db_table': 'DocumentacaoLicenciamento',
                'ordering': ['nome'],
            },
        ),
    ]