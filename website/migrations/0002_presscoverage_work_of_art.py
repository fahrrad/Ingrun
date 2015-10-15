# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presscoverage',
            name='work_of_art',
            field=models.ForeignKey(null=True, to='website.WorkOfArt'),
        ),
    ]
