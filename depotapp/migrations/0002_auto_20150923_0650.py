# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_available',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
