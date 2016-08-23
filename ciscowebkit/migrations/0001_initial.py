# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-19 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACIDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('controllers', models.CharField(max_length=64)),
                ('user', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
