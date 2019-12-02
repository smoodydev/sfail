# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 12:06
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0004_auto_20191125_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='minimun_bidding_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('9999999.99'))]),
            preserve_default=False,
        ),
    ]
