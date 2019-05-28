# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0040_auto_20180801_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laboratory',
            options={'permissions': (('view_laboratory', 'Can see available laboratory'), ('view_report', 'Can see available reports'), ('do_report', 'Can download available reports')), 'verbose_name': 'Laboratory', 'verbose_name_plural': 'Laboratories'},
        ),
        migrations.AlterField(
            model_name='organizationstructure',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='organizationstructure',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='organizationstructure',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]