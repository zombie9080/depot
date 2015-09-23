# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('depotapp', '0004_product_date_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_available',
            field=models.DateField(default=datetime.datetime(2015, 9, 23, 8, 15, 52, 406946)),
        ),
    ]
