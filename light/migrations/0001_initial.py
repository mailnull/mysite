# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lg_rm_zh', models.CharField(unique=True, max_length=4)),
                ('lg_status', models.CharField(default=b'dengGuan', max_length=8)),
                ('lg_room', models.CharField(unique=True, max_length=4)),
                ('lg_flag', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
