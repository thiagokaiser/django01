# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='data_registro',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
    ]
