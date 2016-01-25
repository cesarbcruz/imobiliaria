# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='codigo',
            field=models.CharField(max_length=13, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='imovel',
            name='suites',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
