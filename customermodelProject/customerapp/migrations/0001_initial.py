# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-01-02 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customerinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('cage', models.IntegerField()),
                ('cno', models.IntegerField()),
                ('clocaton', models.CharField(max_length=30)),
            ],
        ),
    ]
