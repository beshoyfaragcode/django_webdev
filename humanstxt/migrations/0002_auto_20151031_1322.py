# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanstxt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='extras',
            field=models.ManyToManyField(blank=True, to='humanstxt.Extra'),
        ),
    ]
