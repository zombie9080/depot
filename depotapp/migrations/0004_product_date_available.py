# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0003_auto_20150923_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_available',
            field=models.DateField(default=datetime.date(2015, 9, 23)),
        ),
    ]
