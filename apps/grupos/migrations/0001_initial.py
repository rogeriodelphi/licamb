# Generated by Django 3.2.7 on 2021-09-27 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divisoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='Código')),
                ('descricao', models.CharField(max_length=110)),
                ('divisao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='divisoes.divisao', verbose_name='Divisão')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'db_table': 'grupo',
                'ordering': ['divisao'],
            },
        ),
    ]
