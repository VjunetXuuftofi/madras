# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-08 12:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0006_auto_20180428_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='RatingResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.RatingField')),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rating_number',
        ),
        migrations.AddField(
            model_name='ratingresponse',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.Rating'),
        ),
    ]