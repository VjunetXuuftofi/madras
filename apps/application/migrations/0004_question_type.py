# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-19 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180415_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
