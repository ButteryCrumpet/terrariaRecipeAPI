# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('ingredients', models.ManyToManyField(to='recipeAPI.Ingredient')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipeAPI.Item')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='as_station', to='recipeAPI.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuckyou', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeAPI.Item'),
        ),
    ]
