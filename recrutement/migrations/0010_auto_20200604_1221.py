# Generated by Django 3.0.6 on 2020-06-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrutement', '0009_critere_recrutement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultat',
            name='critere1',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='critere2',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='critere3',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='critere4',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='resultat',
            name='critere5',
            field=models.PositiveIntegerField(),
        ),
    ]
