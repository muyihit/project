# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20151110_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='hope',
            name='hopesry',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
