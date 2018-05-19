# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-19 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
                ('logo', models.FileField(blank=True, null=True, upload_to=b'')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('audio', models.FileField(blank=True, null=True, upload_to=b'')),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
            ],
        ),
        migrations.AddField(
            model_name='favoritesong',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Song'),
        ),
        migrations.AddField(
            model_name='favoritesong',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
