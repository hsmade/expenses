# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_deposittype'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='type',
            field=models.ForeignKey(default=1, to='expenses.DepositType'),
            preserve_default=False,
        ),
    ]
