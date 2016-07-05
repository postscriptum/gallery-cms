# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_article_enabled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='order',
            field=models.SmallIntegerField(default=10),
        ),
    ]
