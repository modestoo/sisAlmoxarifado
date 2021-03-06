# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_material', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_material', models.CharField(max_length=200)),
                ('tipo_material', models.CharField(max_length=200)),
                ('unidade_medida', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel_pelo_recebimento', models.CharField(max_length=200)),
                ('data_recebimento', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='estoque',
            name='materiais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recebimentoMaterial.Material'),
        ),
    ]
