# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_log_is_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='img_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
