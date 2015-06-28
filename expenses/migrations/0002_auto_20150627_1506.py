# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='account_number',
            field=models.CharField(max_length=34, null=True, verbose_name=b'opposite account number, if any', blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='due_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='account_number',
            field=models.CharField(max_length=34, null=True, verbose_name=b'opposite account number, if any', blank=True),
        ),
    ]
