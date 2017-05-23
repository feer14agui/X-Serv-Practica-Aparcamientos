# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='Num_Comentario',
            field=models.CharField(max_length=10),
        ),
    ]
