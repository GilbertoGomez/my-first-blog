# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='', upload_to='static/imagenes'),
        ),
    ]