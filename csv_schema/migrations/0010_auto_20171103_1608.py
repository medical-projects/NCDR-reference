# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_schema', '0009_datadictionaryreference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadictionaryreference',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
