# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0002_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Members',
        ),
    ]
