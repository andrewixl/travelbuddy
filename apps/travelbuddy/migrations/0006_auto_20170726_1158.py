# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0005_auto_20170726_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='travelenddate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 11, 58, 19, 281000)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='travelstartdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 11, 58, 19, 281000)),
        ),
    ]
