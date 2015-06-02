# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20150602_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='original',
            field=models.CharField(unique=True, max_length=5000),
        ),
    ]
