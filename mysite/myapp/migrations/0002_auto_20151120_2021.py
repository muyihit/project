# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(primary_key=True, serialize=False, auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
