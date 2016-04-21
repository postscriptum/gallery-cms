# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20160420_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='layout',
            field=models.CharField(choices=[('front/grid_3.html', '3 Column Grid'), ('front/grid_4.html', '4 Column Grid'), ('front/slides.html', 'Slides'), ('front/slides_collapsed.html', 'Collapsed Slides')], max_length=50, default='front/grid_3.html'),
        ),
    ]
