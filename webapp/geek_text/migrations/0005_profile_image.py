# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek_text', '0004_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
