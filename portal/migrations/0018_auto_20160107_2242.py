# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20160107_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bairro',
            name='author',
        ),
        migrations.RemoveField(
            model_name='cidade',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tipoimovel',
            name='author',
        ),
    ]
