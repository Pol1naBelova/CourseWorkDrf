# Generated by Django 4.1.2 on 2023-10-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(upload_to='media/films'),
        ),
    ]