# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeAPI', '0002_delete_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]