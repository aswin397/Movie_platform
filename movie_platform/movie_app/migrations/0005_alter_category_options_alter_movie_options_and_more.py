# Generated by Django 4.2.5 on 2024-09-10 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='gross',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='no_of_votes',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default=datetime.datetime(2024, 9, 10, 5, 15, 21, 852505, tzinfo=datetime.timezone.utc), upload_to='posters/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
