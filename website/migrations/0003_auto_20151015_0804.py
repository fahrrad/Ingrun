# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_presscoverage_work_of_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='presscoverage',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presscoverage',
            name='title',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
