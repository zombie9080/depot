# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0005_auto_20150923_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_available',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
