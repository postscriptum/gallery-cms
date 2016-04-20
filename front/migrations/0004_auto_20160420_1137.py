# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20160419_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='layout',
            field=models.CharField(max_length=50, choices=[('table.html', 'Table'), ('collapsed.html', 'Collapsed')], default='table.html'),
        ),
    ]
