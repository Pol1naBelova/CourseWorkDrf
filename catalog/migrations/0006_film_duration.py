# Generated by Django 4.1.2 on 2023-10-08 23:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_film_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
