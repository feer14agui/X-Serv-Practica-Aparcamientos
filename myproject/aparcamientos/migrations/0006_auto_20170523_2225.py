# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0005_auto_20170523_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Contraseña',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Nombre',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
