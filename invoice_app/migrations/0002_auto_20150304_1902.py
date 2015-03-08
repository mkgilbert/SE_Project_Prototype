# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='home_phone',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_phone',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
