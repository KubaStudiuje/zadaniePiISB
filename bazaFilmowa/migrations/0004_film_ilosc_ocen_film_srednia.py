# Generated by Django 4.1.3 on 2022-12-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaFilmowa', '0003_alter_aktor_options_alter_film_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='ilosc_ocen',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='srednia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
