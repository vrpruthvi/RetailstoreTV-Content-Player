# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 08:48
from __future__ import unicode_literals

import cloudinary.models
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
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('disabled', models.BooleanField(default=False)),
                ('sort_order', models.IntegerField(default=100)),
                ('last_check_in', models.DateTimeField(blank=True, null=True)),
                ('login_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.IntegerField(choices=[(1, 'Image'), (2, 'Video')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('image_file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('video_file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('sort_order', models.IntegerField(default=100)),
                ('store', models.ManyToManyField(related_name='content', to='cms.Store')),
            ],
        ),
    ]
