# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-11 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[(b'pxjg', b'\xe5\x9f\xb9\xe8\xae\xad\xe6\x9c\xba\xe6\x9e\x84'), (b'gr', b'\xe4\xb8\xaa\xe4\xba\xba'), (b'gx', b'\xe9\xab\x98\xe6\xa0\xa1')], default=b'pxjg', max_length=20, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xb1\xbb\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to=b'org/%Y/%m', verbose_name=b'logo'),
        ),
    ]
