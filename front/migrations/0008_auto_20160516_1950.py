# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_theme_bg_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='jumbotron_content',
            field=ckeditor.fields.RichTextField(default='', blank=True),
        ),
    ]
