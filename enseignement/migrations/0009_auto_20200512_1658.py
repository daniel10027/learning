# Generated by Django 3.0.5 on 2020-05-12 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enseignement', '0008_auto_20200511_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressourcepdf',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ressourcepdf', to='enseignement.Cours'),
        ),
    ]
