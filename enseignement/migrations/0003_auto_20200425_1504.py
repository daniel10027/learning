# Generated by Django 3.0.5 on 2020-04-25 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enseignement', '0002_auto_20200425_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ufr',
            name='etablissement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etablissement_ufr', to='enseignement.Etablissement'),
        ),
    ]
