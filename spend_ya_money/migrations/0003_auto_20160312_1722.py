# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spend_ya_telegram', '0002_auto_20160312_1721'),
        ('spend_ya_money', '0002_yamoney_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.TextField(unique=True)),
                ('access_token', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('card_id', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spend_ya_telegram.User')),
            ],
        ),
        migrations.DeleteModel(
            name='YaMoney',
        ),
    ]
