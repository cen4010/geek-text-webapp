# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geek_text', '0019_creditcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='user',
        ),
        migrations.DeleteModel(
            name='CreditCard',
        ),
    ]
