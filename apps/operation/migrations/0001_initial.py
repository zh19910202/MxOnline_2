# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=200, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8bc4\u8bba',
                'verbose_name_plural': '\u8bfe\u7a0b\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('mobile', models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('course_name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u54a8\u8be2',
                'verbose_name_plural': '\u7528\u6237\u54a8\u8be2',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8bfe\u7a0b',
                'verbose_name_plural': '\u7528\u6237\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_id', models.IntegerField(default=0, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xaeid')),
                ('fav_type', models.IntegerField(default=1, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xaf\xbe\xe7\xa8\x8b'), (2, b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x9c\xba\xe6\x9e\x84'), (3, b'\xe8\xae\xb2\xe5\xb8\x88')])),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(default=0, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\x97\xe7\x94\xa8\xe6\x88\xb7')),
                ('message', models.CharField(max_length=500, verbose_name=b'\xe6\xb6\x88\xe6\x81\xaf')),
                ('has_read', models.BooleanField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xb7\xb2\xe8\xaf\xbb')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6d88\u606f',
                'verbose_name_plural': '\u7528\u6237\u6d88\u606f',
            },
        ),
    ]
