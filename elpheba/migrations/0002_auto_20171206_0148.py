# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elpheba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='BuyPoint',
            field=models.PositiveIntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='SellPoint',
            field=models.PositiveIntegerField(default=85),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='bufferEquity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='closeTrades',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='dp',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='instant_close',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='max_trades',
            field=models.PositiveIntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='openTrades',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='sl',
            field=models.PositiveIntegerField(default=75000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='tp',
            field=models.PositiveIntegerField(default=200),
            preserve_default=False,
        ),
    ]
