# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-31 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20170829_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemkind',
            name='category',
            field=models.SmallIntegerField(choices=[(0, 'Scheduled'), (1, 'Authorized')], default=0, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_spec', to='collection.ItemSpec', verbose_name='Spec'),
        ),
        migrations.AlterField(
            model_name='itemspec',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_kind', to='collection.ItemKind', verbose_name='Kind'),
        ),
        migrations.AlterField(
            model_name='itemspec',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Spec'),
        ),
    ]