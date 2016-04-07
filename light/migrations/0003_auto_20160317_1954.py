# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0002_espsertime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lightstatus',
            options={'verbose_name': '\u7167\u660e'},
        ),
    ]
