# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-18 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrotrade', '0003_favoriteask_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerasks',
            name='payment_methods',
            field=models.ManyToManyField(blank=True, to='agrotrade.PaymentMethod'),
        ),
    ]
