# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_remove_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home', models.CharField(max_length=50, blank=True)),
                ('goal', models.CharField(max_length=50, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('busy', models.IntegerField(default=0, choices=[(1, b'\xe5\xbf\x99\xe7\xa2\x8c'), (0, b'\xe7\xa9\xba\xe9\x97\xb2')])),
                ('tip', models.CharField(max_length=128, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='busy',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='home',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='price',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tip',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='user',
        ),
    ]
