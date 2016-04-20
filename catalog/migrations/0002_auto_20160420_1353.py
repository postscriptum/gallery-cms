# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='galleries',
            field=models.ManyToManyField(blank=True, to='catalog.Gallery'),
        ),
    ]
