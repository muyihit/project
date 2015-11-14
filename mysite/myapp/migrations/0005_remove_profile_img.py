# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_profile_is_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
    ]
