# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-01 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_shop_wheel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('isselect', models.BooleanField(default=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
    ]
