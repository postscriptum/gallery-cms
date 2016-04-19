# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20160419_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='header_text',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='jumbotron_content',
        ),
        migrations.AddField(
            model_name='general',
            name='footer_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='general',
            name='header_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='general',
            name='jumbotron_content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
