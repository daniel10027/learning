# Generated by Django 3.0.5 on 2020-04-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enseignement', '0001_initial'),
        ('gestion', '0002_auto_20200424_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='niveaut',
        ),
        migrations.AddField(
            model_name='student',
            name='niveaux',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enseignement.Niveau'),
        ),
        migrations.AlterField(
            model_name='student',
            name='etablissemnt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enseignement.Etablissement'),
        ),
        migrations.AlterField(
            model_name='student',
            name='specialite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enseignement.Specialite'),
        ),
    ]