# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_remove_month_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('due_date', models.DateField(null=True, blank=True)),
                ('month', models.ForeignKey(to='expenses.Month')),
            ],
        ),
    ]
