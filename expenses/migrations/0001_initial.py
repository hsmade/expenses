# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('date', models.DateField(verbose_name=b'date deposited')),
                ('account_number', models.CharField(max_length=34, verbose_name=b'opposite account number, if any', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('balance', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('due_date', models.DateField(blank=True)),
                ('automatic_increase', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('date', models.DateField(verbose_name=b'date deposited')),
                ('account_number', models.CharField(max_length=34, verbose_name=b'opposite account number, if any', blank=True)),
                ('month', models.ForeignKey(to='expenses.Month')),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='type',
            field=models.ForeignKey(to='expenses.WithdrawalType'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='month',
            field=models.ForeignKey(to='expenses.Month'),
        ),
    ]
