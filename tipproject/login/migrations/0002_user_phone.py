# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=18539300000, max_length=256),
            preserve_default=False,
        ),
    ]