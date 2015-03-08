# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_auto_20150304_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='home_phone',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_phone',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
