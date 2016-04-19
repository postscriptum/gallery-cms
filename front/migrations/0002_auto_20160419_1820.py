# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='footer_text',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='header_text',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='jumbotron',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='theme',
            name='jumbotron_content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='theme',
            name='layout',
            field=models.SmallIntegerField(choices=[(1, 'Aaa'), (2, 'Bbb'), (3, 'Ccc')], default=1),
        ),
    ]
