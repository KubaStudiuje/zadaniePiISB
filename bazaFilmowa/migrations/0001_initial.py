# Generated by Django 4.1.3 on 2022-12-14 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwsiko', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Aktor',
                'verbose_name_plural': 'Aktorzy',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
                ('opis', models.TextField()),
                ('slug', models.SlugField(default='film', max_length=45)),
                ('premiera', models.DateField(verbose_name='premiera')),
                ('aktorzy', models.ManyToManyField(to='bazaFilmowa.aktor')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
            },
        ),
        migrations.CreateModel(
            name='Rezyser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwsiko', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Reżyser',
                'verbose_name_plural': 'Reżyserzy',
            },
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('wartosc', models.IntegerField(choices=[(1, 'Tragiczn'), (2, 'Ujdzie'), (3, 'Sredni'), (4, 'Dobry'), (5, 'Swietny')])),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazaFilmowa.film')),
            ],
            options={
                'verbose_name': 'Ocena',
                'verbose_name_plural': 'Oceny',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='rezyser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazaFilmowa.rezyser'),
        ),
    ]
