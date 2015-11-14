# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_img',
            field=models.IntegerField(default=0),
        ),
    ]
