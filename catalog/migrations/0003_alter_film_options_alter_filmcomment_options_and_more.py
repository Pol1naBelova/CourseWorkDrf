# Generated by Django 4.1.2 on 2023-10-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_film_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='filmcomment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterModelOptions(
            name='profiletickets',
            options={'verbose_name': 'Билеты в профиле', 'verbose_name_plural': 'Билеты в профилях'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
