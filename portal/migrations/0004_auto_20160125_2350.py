# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20160125_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='codigo',
            field=models.CharField(unique=True, max_length=13),
        ),
    ]
