# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryUsers',
            new_name='GalleryUser',
        ),
    ]
