# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20151108_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='hope',
            name='landtype',
            field=models.CharField(default=b'any', max_length=10, verbose_name=b'\xe7\x9b\xae\xe7\x9a\x84\xe5\x9c\xb0\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'any', b'\xe9\x9a\x8f\xe6\x84\x8f'), (b'plain', b'\xe5\xb9\xb3\xe5\x8e\x9f'), (b'mountain', b'\xe5\xb1\xb1\xe6\x9e\x97'), (b'water', b'\xe6\xb9\x96\xe6\xb5\xb7'), (b'interest', b'\xe5\x90\x8d\xe8\x83\x9c'), (b'scenery', b'\xe6\x99\xaf\xe5\x8c\xba'), (b'explore', b'\xe6\x8e\xa2\xe9\x99\xa9')]),
        ),
        migrations.AlterField(
            model_name='hope',
            name='busy',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa9\xba\xe9\x97\xb2', choices=[(1, b'\xe5\xbf\x99\xe7\xa2\x8c'), (0, b'\xe7\xa9\xba\xe9\x97\xb2')]),
        ),
    ]
