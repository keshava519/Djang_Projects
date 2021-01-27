# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-01-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=256)),
            ],
        ),
    ]
