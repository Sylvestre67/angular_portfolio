# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='zzmigrations', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliopost',
            name='slug',
            field=models.CharField(default='zzmigrations', max_length=256),
            preserve_default=False,
        ),
    ]