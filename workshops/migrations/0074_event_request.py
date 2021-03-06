# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0073_auto_20160127_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='request',
            field=models.ForeignKey(blank=True, help_text='Backlink to the request that created this event.', null=True, on_delete=django.db.models.deletion.CASCADE, to='workshops.EventRequest'),
        ),
    ]
