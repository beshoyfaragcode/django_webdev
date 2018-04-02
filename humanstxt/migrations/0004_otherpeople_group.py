# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanstxt', '0003_otherpeople'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherpeople',
            name='group',
            field=models.ForeignKey(blank=True, to='humanstxt.Group', null=True,on_delete=models.DO_NOTHING),
        ),
    ]
