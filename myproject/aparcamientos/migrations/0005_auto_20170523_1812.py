# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0004_auto_20170522_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Color',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='Tamano',
            field=models.FloatField(default=11),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='Num_Comentario',
            field=models.IntegerField(default=0),
        ),
    ]
