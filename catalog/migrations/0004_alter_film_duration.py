# Generated by Django 4.1.2 on 2023-10-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_film_options_alter_filmcomment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.DurationField(),
        ),
    ]
