# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_short_blog_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='absolute_url',
            field=models.CharField(blank=True, editable=False, max_length=400),
        ),
    ]
