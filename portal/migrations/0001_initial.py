# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import portal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio_divulgacao', models.DateTimeField(null=True, blank=True)),
                ('data_final_divulgacao', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logradouro', models.TextField()),
                ('quartos', models.IntegerField(null=True, blank=True)),
                ('banheiro', models.IntegerField(null=True, blank=True)),
                ('vagas_garagem', models.IntegerField(null=True, blank=True)),
                ('valor', models.DecimalField(max_digits=8, decimal_places=2)),
                ('area_construida', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('area_total', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('descricao', models.TextField()),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_divulgacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo_negociacao', models.CharField(max_length=1, choices=[(b'0', b'Aluguel'), (b'1', b'Venda')])),
                ('foto_1', models.ImageField(upload_to=portal.models.sample_upload_to_function)),
                ('foto_2', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_3', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_4', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_5', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_6', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_7', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('foto_8', models.ImageField(null=True, upload_to=portal.models.sample_upload_to_function, blank=True)),
                ('bairro', models.ForeignKey(to='portal.Bairro')),
            ],
            options={
                'verbose_name_plural': 'Imoveis',
            },
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=12)),
                ('telefone_fixo', models.CharField(max_length=13, null=True, blank=True)),
                ('celular_1', models.CharField(max_length=13, null=True, blank=True)),
                ('celular_2', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('telefone_comercial', models.CharField(max_length=13, null=True, blank=True)),
                ('usuario', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=255)),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Tipo Imoveis',
            },
        ),
        migrations.AddField(
            model_name='imovel',
            name='proprietario',
            field=models.ForeignKey(to='portal.Proprietario'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo',
            field=models.ForeignKey(to='portal.TipoImovel'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='usuario',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='destaque',
            name='imovel',
            field=models.ForeignKey(to='portal.Imovel'),
        ),
        migrations.AddField(
            model_name='destaque',
            name='usuario',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(to='portal.Cidade'),
        ),
    ]
