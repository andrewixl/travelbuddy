# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 17:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0003_auto_20170726_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='travelenddate',
            field=models.DateField(default=datetime.datetime(2017, 7, 26, 10, 26, 14, 624000)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='travelstartdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 26, 10, 26, 14, 624000)),
        ),
    ]
