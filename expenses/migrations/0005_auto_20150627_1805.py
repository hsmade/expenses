# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_deposit_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='type',
            new_name='deposit_type',
        ),
        migrations.RenameField(
            model_name='withdrawal',
            old_name='type',
            new_name='withdrawal_type',
        ),
    ]
