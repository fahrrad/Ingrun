# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressCoverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOfArt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('workofart_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='website.WorkOfArt')),
            ],
            options={
                'verbose_name': 'Exhibition',
            },
            bases=('website.workofart',),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('workofart_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='website.WorkOfArt')),
            ],
            options={
                'verbose_name': 'Movie',
            },
            bases=('website.workofart',),
        ),
        migrations.CreateModel(
            name='TheaterPlay',
            fields=[
                ('workofart_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='website.WorkOfArt')),
            ],
            options={
                'verbose_name': 'Theater Play',
            },
            bases=('website.workofart',),
        ),
    ]
