# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=30)),
                ('upwd', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=50)),
                ('uemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
