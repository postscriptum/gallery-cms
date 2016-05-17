# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_auto_20160516_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='panel_bg_color',
            field=colorful.fields.RGBColorField(default='#C0C0C0'),
        ),
        migrations.AddField(
            model_name='theme',
            name='panel_text_color',
            field=colorful.fields.RGBColorField(default='#000000'),
        ),
    ]
