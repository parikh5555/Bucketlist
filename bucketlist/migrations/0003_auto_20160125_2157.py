# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0002_auto_20151221_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='bucketlistitem',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]