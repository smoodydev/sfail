# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-05 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0006_auto_20191203_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='bidding_time',
            new_name='end_date',
        ),
    ]
