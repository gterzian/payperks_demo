# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='shortened',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
