# Generated by Django 3.0.5 on 2020-04-27 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recrutement', '0005_auto_20200427_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diplome',
            old_name='dossier',
            new_name='fichier',
        ),
    ]
