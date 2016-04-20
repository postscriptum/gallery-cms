# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20160420_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='layout',
            field=models.CharField(default='front/table.html', max_length=50, choices=[('front/table.html', 'Table'), ('front/collapsed.html', 'Collapsed')]),
        ),
    ]
