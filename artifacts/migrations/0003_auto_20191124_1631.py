# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0002_auto_20191119_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='by_user',
            field=models.IntegerField(default=1),
        ),
    ]
