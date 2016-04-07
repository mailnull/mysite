# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawsfan', '0003_auto_20160317_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawstatus',
            name='rawmode',
            field=models.CharField(help_text='\u5236\u70ed|\u5236\u51b7', max_length=3, verbose_name='\u72b6\u6001\u6a21\u5f0f'),
            preserve_default=True,
        ),
    ]
