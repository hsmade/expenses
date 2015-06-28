# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20150627_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
