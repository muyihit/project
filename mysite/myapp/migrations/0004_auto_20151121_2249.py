# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_log_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
