# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0030_laboratory_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratory.OrganizationStructure'),
        ),
    ]
