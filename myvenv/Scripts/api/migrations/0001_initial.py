# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-06 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk_ID', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Speaker', models.CharField(max_length=200)),
                ('Venue', models.CharField(max_length=200)),
                ('Duration', models.CharField(max_length=200)),
            ],
        ),
    ]
