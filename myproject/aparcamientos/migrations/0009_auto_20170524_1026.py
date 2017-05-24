# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0008_auto_20170524_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Tamano',
            field=models.FloatField(default=5),
        ),
    ]
