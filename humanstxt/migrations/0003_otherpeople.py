# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanstxt', '0002_auto_20151031_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('extras', models.ManyToManyField(to='humanstxt.Extra', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
