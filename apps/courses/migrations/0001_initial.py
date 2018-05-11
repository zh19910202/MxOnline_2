# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d')),
                ('desc', models.CharField(max_length=300, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('detail', models.TextField(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe8\xaf\xa6\xe6\x83\x85')),
                ('degree', models.CharField(max_length=2, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe9\x9a\xbe\xe5\xba\xa6', choices=[(b'cj', b'\xe5\x88\x9d\xe7\xba\xa7'), (b'zj', b'\xe9\xab\x98\xe7\xba\xa7'), (b'gj', b'\xe9\xab\x98\xe7\xba\xa7')])),
                ('learn_times', models.IntegerField(default=0, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe6\x97\xb6\xe9\x95\xbf(\xe5\x88\x86\xe9\x92\x9f\xe6\x95\xb0)')),
                ('students', models.IntegerField(default=0, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe4\xba\xba\xe6\x95\xb0')),
                ('fav_nums', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe4\xba\xba\xe6\x95\xb0')),
                ('image', models.ImageField(upload_to=b'courses/%Y/%m', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe')),
                ('click_nums', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\xbe\xe4\xbb\xb6\xe5\x90\x8d')),
                ('download', models.FileField(upload_to=b'course/resource/%Y/%m', verbose_name=b'\xe8\xb5\x84\xe6\xba\x90\xe6\x96\x87\xe4\xbb\xb6')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe8\xaf\xbe\xe4\xbb\xb6\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('course', models.ForeignKey(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', to='courses.Course')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8d44\u6e90',
                'verbose_name_plural': '\u8bfe\u7a0b\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe7\xab\xa0\xe8\x8a\x82\xe5\x90\x8d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe7\xab\xa0\xe8\x8a\x82\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('course', models.ForeignKey(verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', to='courses.Course')),
            ],
            options={
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe5\x90\x8d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('lesson', models.ForeignKey(verbose_name=b'\xe7\xab\xa0\xe8\x8a\x82', to='courses.Lesson')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]
