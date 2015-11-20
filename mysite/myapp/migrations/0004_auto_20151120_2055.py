# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20151120_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hope',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='price',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
