# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geek_text', '0006_auto_20180418_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
    ]
