# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 17:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='travelenddate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 10, 14, 57, 375000)),
        ),
        migrations.AddField(
            model_name='plan',
            name='travelstartdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 10, 14, 57, 375000)),
        ),
    ]
