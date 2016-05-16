# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_auto_20160421_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='bg_color',
            field=colorful.fields.RGBColorField(default='#FFFFFF'),
        ),
    ]
