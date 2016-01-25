# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20160125_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='codigo',
            field=models.CharField(default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='valor',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
    ]
