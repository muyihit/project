# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20151108_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hope',
            name='home',
            field=models.CharField(blank=True, max_length=50, error_messages={b'required': b'\xe5\x87\xba\xe5\x8f\x91\xe5\x9c\xb0\xe4\xb8\x80\xe5\xae\x9a\xe8\xa6\x81\xe5\x86\x99\xe5\x93\xa6'}),
        ),
    ]
