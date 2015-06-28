# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='budget',
            field=models.ManyToManyField(to='expenses.Budget'),
        ),
    ]
