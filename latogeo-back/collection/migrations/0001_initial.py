# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patrimony', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Patrimony')),
            ],
        ),
        migrations.CreateModel(
            name='ItemKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kind')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Model')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_kind', to='collection.ItemKind', verbose_name='Kind')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_model', to='collection.ItemModel', verbose_name='Model'),
        ),
    ]