# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-09 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_application_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('application', 'question')]),
        ),
    ]