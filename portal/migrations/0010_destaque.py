# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0009_auto_20151219_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio_divulgacao', models.DateTimeField(blank=True, null=True)),
                ('data_final_divulgacao', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Imovel')),
            ],
        ),
    ]