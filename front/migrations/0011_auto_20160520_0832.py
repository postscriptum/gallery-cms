# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_theme_text_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='jumbotron_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='theme',
            name='layout',
            field=models.CharField(max_length=50, default='front/grid_3.html', choices=[('front/grid_3.html', '3-Column Grid'), ('front/grid_4.html', '4-Column Grid'), ('front/grid_6.html', '6-Column Grid')]),
        ),
    ]
