# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-14 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0013_auto_20180614_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]