# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0003_auto_20160317_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='espsertime',
            options={'verbose_name': 'ESP\u65f6\u95f4', 'verbose_name_plural': 'ESP\u65f6\u95f4'},
        ),
        migrations.AlterModelOptions(
            name='lightstatus',
            options={'verbose_name': '\u7167\u660e', 'verbose_name_plural': '\u7167\u660e'},
        ),
    ]
