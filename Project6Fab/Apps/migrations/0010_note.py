# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0009_auto_20190212_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.CharField(max_length=300)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.HomeModel')),
            ],
        ),
    ]