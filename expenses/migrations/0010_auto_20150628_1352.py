# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_auto_20150627_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawaltype',
            name='max_allowed',
            field=models.IntegerField(default=0),
        ),
    ]
