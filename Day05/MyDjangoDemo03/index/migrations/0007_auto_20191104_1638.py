# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-11-04 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20191104_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-publicate_date'], 'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/uploda', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, verbose_name='书名'),
        ),
    ]
