# Generated by Django 3.2.7 on 2021-10-23 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211018_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='foto',
            new_name='photo',
        ),
    ]
