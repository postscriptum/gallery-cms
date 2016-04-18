# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('under_construction', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('header', models.BooleanField(default=False)),
                ('footer', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='general',
            name='theme',
            field=models.ForeignKey(to='front.Theme', blank=True, null=True),
        ),
    ]
