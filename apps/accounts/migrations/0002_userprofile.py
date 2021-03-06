# Generated by Django 3.2.7 on 2021-09-27 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='photos', verbose_name='Foto')),
                ('celular', models.CharField(max_length=16, verbose_name='Celular')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil do Usuário',
                'verbose_name_plural': 'Perfis dos usuários',
                'db_table': 'UserProfile',
            },
        ),
    ]
