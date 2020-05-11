# Generated by Django 3.0.5 on 2020-05-11 18:35

from django.db import migrations, models
import gestion.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20200511_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuteur',
            name='photo',
            field=models.FileField(default='none.png', upload_to='tuteurs/photos/', validators=[gestion.models.validate_file_extension_for_image]),
        ),
        migrations.AlterField(
            model_name='tuteur',
            name='piece_indentite',
            field=models.FileField(default='none.png', upload_to='tuteurs/pieces/', validators=[gestion.models.validate_file_extension_for_document]),
        ),
    ]
