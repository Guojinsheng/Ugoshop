# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-26 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
