# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20160414_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='', upload_to='', width_field='300'),
        ),
    ]