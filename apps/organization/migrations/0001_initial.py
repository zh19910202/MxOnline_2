# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82\xe5\x90\x8d')),
                ('desc', models.CharField(max_length=200, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('click_nums', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('fav_nums', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0')),
                ('image', models.ImageField(upload_to=b'org/%Y/%m')),
                ('address', models.CharField(max_length=150, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9c\xb0\xe5\x9d\x80')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe5\x9f\x8e\xe5\xb8\x82', to='organization.CityDict')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u673a\u6784',
                'verbose_name_plural': '\u8bfe\u7a0b\u673a\u6784',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe5\x90\x8d')),
                ('wrok_years', models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xb9\xb4\xe9\x99\x90')),
                ('wrok_company', models.CharField(max_length=50, verbose_name=b'\xe5\xb0\xb1\xe8\x81\x8c\xe5\x85\xac\xe5\x8f\xb8')),
                ('wrok_position', models.CharField(max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe8\x81\x8c\xe4\xbd\x8d')),
                ('points', models.CharField(max_length=50, verbose_name=b'\xe6\x95\x99\xe5\xad\xa6\xe7\x89\xb9\xe7\x82\xb9')),
                ('click_nums', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('fav_nums', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='organization.CourseOrg')),
            ],
            options={
                'verbose_name': '\u6559\u5e08',
                'verbose_name_plural': '\u6559\u5e08',
            },
        ),
    ]
