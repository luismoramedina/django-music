# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400, verbose_name='name')),
                ('author', models.CharField(max_length=400, verbose_name='author')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
            },
        ),
    ]