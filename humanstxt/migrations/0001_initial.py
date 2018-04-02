# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('field_name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
                ('location', models.CharField(null=True, max_length=512, blank=True)),
                ('email', models.EmailField(null=True, max_length=256, blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('extras', models.ManyToManyField(null=True, to='humanstxt.Extra')),
                ('group', models.ForeignKey(blank=True, to='humanstxt.Group', null=True,on_delete=models.DO_NOTHING)),
            ],
            options={
                'ordering': ['order', 'last_name'],
            },
        ),
    ]
