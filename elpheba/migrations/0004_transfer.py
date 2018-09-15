# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elpheba', '0003_account_banked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctNumber', models.PositiveIntegerField()),
                ('withdrawls', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]