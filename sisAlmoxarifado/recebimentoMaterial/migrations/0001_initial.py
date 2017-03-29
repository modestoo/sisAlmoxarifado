# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_material', models.CharField(max_length=200)),
                ('tipo_material', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='setorRequisitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_setorRequisitante', models.CharField(max_length=200)),
            ],
        ),
    ]
