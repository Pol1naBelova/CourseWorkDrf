# Generated by Django 4.1.2 on 2023-10-08 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_film_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=7205)),
            preserve_default=False,
        ),
    ]
