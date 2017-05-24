# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0006_auto_20170523_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fecha',
            name='Usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
