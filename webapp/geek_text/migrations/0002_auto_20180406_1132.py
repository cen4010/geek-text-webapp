# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek_text', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=8),
        ),
    ]
