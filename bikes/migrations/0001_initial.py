# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('bike_make', models.CharField(max_length=100)),
                ('bike_model', models.CharField(max_length=100)),
                ('bike_type', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('wheel_diameter', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CassetteSprocket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField()),
                ('bike', models.ForeignKey(to='bikes.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='Chainring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField()),
                ('bike', models.ForeignKey(to='bikes.Bike')),
            ],
        ),
    ]
