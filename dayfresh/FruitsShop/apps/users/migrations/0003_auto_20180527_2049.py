# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_fruitsusers_u_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitsusers',
            name='u_name',
            field=models.CharField(default='小花', max_length=50, verbose_name='收件人'),
        ),
    ]
