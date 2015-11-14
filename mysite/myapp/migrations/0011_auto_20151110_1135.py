# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20151108_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='travellike',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='home',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
