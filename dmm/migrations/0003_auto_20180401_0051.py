# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmm', '0002_auto_20180330_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts_data',
            name='main_category',
        ),
        migrations.RemoveField(
            model_name='posts_data',
            name='sub_category',
        ),
    ]
