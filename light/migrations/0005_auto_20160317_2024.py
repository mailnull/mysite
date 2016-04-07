# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0004_auto_20160317_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightstatus',
            name='lg_flag',
            field=models.CharField(max_length=1, verbose_name='\u72b6\u6001'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightstatus',
            name='lg_rm_zh',
            field=models.CharField(unique=True, max_length=4, verbose_name='\u623f\u95f4\u540d\u79f0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightstatus',
            name='lg_room',
            field=models.CharField(unique=True, max_length=4, verbose_name='\u623f\u95f4\u540d\u79f0\u82f1\u6587'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightstatus',
            name='lg_status',
            field=models.CharField(default=b'dengGuan', max_length=8, verbose_name='\u72b6\u6001\u82f1\u6587'),
            preserve_default=True,
        ),
    ]
