# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-14 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0011_auto_20180612_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='pic',
            new_name='image',
        ),
    ]