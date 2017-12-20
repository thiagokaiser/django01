# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20171208_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=800)),
                ('data_registro', models.DateField(verbose_name='Data')),
            ],
        ),
    ]
