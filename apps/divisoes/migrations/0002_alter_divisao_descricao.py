# Generated by Django 3.2.7 on 2021-10-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisao',
            name='descricao',
            field=models.CharField(max_length=80),
        ),
    ]