# Generated by Django 3.0.5 on 2020-04-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrutement', '0003_auto_20200426_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='jury',
            name='dossier',
            field=models.ManyToManyField(related_name='dossierjury', to='recrutement.DossierRecrutement'),
        ),
    ]
