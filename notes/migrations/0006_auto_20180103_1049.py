# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20171213_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='descricao',
            field=models.CharField(max_length=800, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='responsavel',
            field=models.CharField(max_length=80, verbose_name='Codigo'),
        ),
    ]