# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-01 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'A lot of Subcribers',
                'verbose_name': 'MySubcriber',
            },
        ),
    ]
