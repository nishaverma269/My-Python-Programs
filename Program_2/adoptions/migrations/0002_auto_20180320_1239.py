# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(null=True)),
                ('PK', models.TextField()),
                ('CCR', models.TextField()),
                ('AGE', models.TextField()),
                ('GENDER', models.TextField()),
                ('RACE', models.TextField()),
                ('ARRESTTIME', models.TextField()),
                ('ARRESTLOCATION', models.IntegerField()),
                ('OFFENSES', models.TextField()),
                ('INCIDENTLOCATION', models.TextField()),
                ('INCIDENTNEIGHBORHOOD', models.TextField()),
                ('INCIDENTZONE', models.TextField()),
                ('INCIDENTTRACT', models.TextField()),
                ('COUNCIL_DISTRICT', models.TextField()),
                ('PUBLIC_WORKS_DIVISION', models.TextField()),
                ('X', models.IntegerField(null=True)),
                ('Y', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pet',
            name='vaccinations',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
        migrations.DeleteModel(
            name='Vaccine',
        ),
    ]