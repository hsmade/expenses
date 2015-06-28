# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_withdrawal_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='month',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='budget',
        ),
        migrations.AddField(
            model_name='withdrawaltype',
            name='max_allowed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
    ]
