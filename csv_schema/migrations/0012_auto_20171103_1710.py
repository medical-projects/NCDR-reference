# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_schema', '0011_auto_20171103_1618'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='datadictionaryreference',
            unique_together=set([('row', 'name')]),
        ),
    ]
