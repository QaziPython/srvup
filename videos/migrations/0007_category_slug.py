# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20160618_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]
