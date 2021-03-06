# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-14 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0012_auto_20180614_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile_pic',
            name='p_pic',
            field=models.FileField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
