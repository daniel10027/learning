# Generated by Django 3.0.5 on 2020-04-24 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20200424_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='niveaux',
            new_name='niveau',
        ),
    ]
