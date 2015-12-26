# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='content',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='describe',
            name='content',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='goal',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='home',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='hopesry',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='hope',
            name='tip',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='img_name',
            field=models.CharField(default=b'', max_length=1000),
        ),
        migrations.AlterField(
            model_name='log',
            name='title',
            field=models.CharField(max_length=1000, verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe9\xa2\x98\xe7\x9b\xae'),
        ),
        migrations.AlterField(
            model_name='logimg',
            name='name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='answer',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qq',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='question',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='travellike',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='content',
            field=models.CharField(max_length=1000, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=1000, verbose_name=b'\xe6\x99\xaf\xe7\x82\xb9\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='sitecommit',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='siteimg',
            name='name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
