# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-11 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0008_auto_20180611_2344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={},
        ),
        migrations.AlterField(
            model_name='box',
            name='content',
            field=models.TextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='box',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
