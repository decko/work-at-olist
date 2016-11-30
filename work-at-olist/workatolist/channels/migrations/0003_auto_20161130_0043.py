# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_uniqueidentifier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UniqueIdentifier',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='id',
        ),
        migrations.AddField(
            model_name='channel',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]