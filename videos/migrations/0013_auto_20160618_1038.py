# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20160618_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='share_message',
            field=models.TextField(default='Check out this awesome video.'),
        ),
    ]
