# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek_text', '0012_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=12, null=True),
        ),
    ]