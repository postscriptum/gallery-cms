# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
