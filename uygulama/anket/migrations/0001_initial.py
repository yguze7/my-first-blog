# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru', models.CharField(max_length=100)),
                ('yayinTarihi', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Secenek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secenek', models.CharField(max_length=100)),
                ('oySayisi', models.PositiveIntegerField(default=0)),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anket.Anket')),
            ],
        ),
    ]
