# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0002_auto_20170522_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='Num_Comentario',
            field=models.IntegerField(default=0),
        ),
    ]
