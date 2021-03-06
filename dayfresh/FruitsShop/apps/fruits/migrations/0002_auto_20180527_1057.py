# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 10:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fruits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='comm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruits.CommInfo', verbose_name='订单商品'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruits.CommOrders', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='commorders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='comminfo',
            name='tags',
            field=models.ManyToManyField(to='fruits.CommTags', verbose_name='商品标签'),
        ),
        migrations.AddField(
            model_name='comminfo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruits.CommType', verbose_name='商品分类'),
        ),
    ]
