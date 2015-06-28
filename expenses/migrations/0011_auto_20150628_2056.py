# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20150628_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='deposit_type',
            field=models.ForeignKey(default=None, blank=True, to='expenses.DepositType', null=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='withdrawal_type',
            field=models.ForeignKey(default=None, blank=True, to='expenses.WithdrawalType', null=True),
        ),
    ]
