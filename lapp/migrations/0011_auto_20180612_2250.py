# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-12 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0010_auto_20180612_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_pic',
            old_name='profile_pic',
            new_name='p_pic',
        ),
    ]
