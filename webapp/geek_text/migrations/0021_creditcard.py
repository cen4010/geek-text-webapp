# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geek_text', '0020_auto_20180420_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(default='', max_length=36)),
                ('card_number', models.CharField(default='', max_length=26)),
                ('card_expirydate', models.DateField(blank=True, null=True)),
                ('card_ccv', models.CharField(default='', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditcard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]