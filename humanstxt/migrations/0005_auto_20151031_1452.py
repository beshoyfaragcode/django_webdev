# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanstxt', '0004_otherpeople_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otherpeople',
            options={'verbose_name_plural': 'Other people'},
        ),
        migrations.AddField(
            model_name='otherpeople',
            name='text',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
