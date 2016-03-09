# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rawmode', models.CharField(max_length=3)),
                ('rawtemp', models.CharField(max_length=2, blank=True)),
                ('timestamp', models.DateTimeField()),
                ('rawtemp1', models.CharField(default=b'25', max_length=2)),
                ('room', models.CharField(unique=True, max_length=4)),
                ('rm_en', models.CharField(unique=True, max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
