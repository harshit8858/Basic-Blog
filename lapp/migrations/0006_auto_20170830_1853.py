# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0005_auto_20170830_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='count',
            field=models.CharField(default='no', max_length=20),
        ),
    ]
