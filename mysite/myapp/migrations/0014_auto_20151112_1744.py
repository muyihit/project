# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hope',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='hope',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
