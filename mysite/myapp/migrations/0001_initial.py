# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe9\xa2\x98\xe7\x9b\xae')),
                ('content', models.CharField(max_length=1000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('date', models.DateTimeField(primary_key=True, serialize=False, auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=16, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.IntegerField(default=1, choices=[(1, b'\xe7\x94\xb7'), (0, b'\xe5\xa5\xb3')])),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('qq', models.CharField(max_length=20, blank=True)),
                ('home', models.CharField(max_length=50, blank=True)),
                ('goal', models.CharField(max_length=50, blank=True)),
                ('date', models.DateField(blank=True)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('busy', models.IntegerField(default=0, choices=[(1, b'\xe5\xbf\x99\xe7\xa2\x8c'), (0, b'\xe7\xa9\xba\xe9\x97\xb2')])),
                ('tip', models.CharField(max_length=128, blank=True)),
                ('question', models.CharField(max_length=50, blank=True)),
                ('answer', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('siteID', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(primary_key=True, serialize=False, auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
