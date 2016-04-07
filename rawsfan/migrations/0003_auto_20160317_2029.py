# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawsfan', '0002_auto_20160317_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawstatus',
            name='rawmode',
            field=models.CharField(max_length=3, verbose_name='\u6a21\u5f0f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rawstatus',
            name='rawtemp',
            field=models.CharField(max_length=2, verbose_name='\u6e29\u5ea6', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rawstatus',
            name='rawtemp1',
            field=models.CharField(default=b'25', max_length=2, verbose_name='\u9ed8\u8ba4\u6e29\u5ea6'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rawstatus',
            name='rm_en',
            field=models.CharField(unique=True, max_length=4, verbose_name='\u623f\u95f4\u82f1\u6587'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rawstatus',
            name='room',
            field=models.CharField(unique=True, max_length=4, verbose_name='\u623f\u95f4\u540d\u79f0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rawstatus',
            name='timestamp',
            field=models.DateTimeField(verbose_name='\u65f6\u95f4'),
            preserve_default=True,
        ),
    ]
