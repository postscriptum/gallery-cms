# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_auto_20160517_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='text_color',
            field=colorful.fields.RGBColorField(default='#000000'),
        ),
    ]
