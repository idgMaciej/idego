# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20170114_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 17, 19, 12, 1, 651035, tzinfo=utc), verbose_name='date_add'),
        ),
    ]
