# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-07 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('mision', models.CharField(blank=True, max_length=1000, null=True)),
                ('vision', models.CharField(blank=True, max_length=1000, null=True)),
                ('eslogan', models.CharField(blank=True, max_length=200, null=True)),
                ('aboutme', models.CharField(blank=True, max_length=1000, null=True)),
                ('logo', models.CharField(blank=True, max_length=200, null=True)),
                ('video', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'web',
                'managed': False,
            },
        ),
    ]