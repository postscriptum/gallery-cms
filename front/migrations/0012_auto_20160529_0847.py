# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_auto_20160520_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='footer_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='layout',
            field=models.CharField(default='front/grid_3.html', max_length=50, choices=[('front/grid_3.html', '3-Column Grid'), ('front/grid_4.html', '4-Column Grid'), ('front/grid_6.html', '6-Column Grid'), ('front/slides.html', 'Slides')]),
        ),
    ]
