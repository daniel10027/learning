# Generated by Django 3.0.6 on 2020-06-03 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recrutement', '0008_critere'),
    ]

    operations = [
        migrations.AddField(
            model_name='critere',
            name='recrutement',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='criteres', to='recrutement.Recrutement'),
            preserve_default=False,
        ),
    ]