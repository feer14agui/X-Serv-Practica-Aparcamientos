# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(max_length=32)),
                ('Nombre', models.TextField()),
                ('Nombre_via', models.CharField(max_length=32)),
                ('Clase_vial', models.CharField(max_length=32)),
                ('Numero', models.CharField(max_length=32)),
                ('Localidad', models.CharField(max_length=32)),
                ('Provincia', models.CharField(max_length=32)),
                ('Cod_Postal', models.CharField(max_length=32)),
                ('Barrio', models.CharField(max_length=32)),
                ('Distrito', models.CharField(max_length=32)),
                ('Coord_X', models.CharField(max_length=32)),
                ('Coord_Y', models.CharField(max_length=32)),
                ('Enlace', models.CharField(max_length=256)),
                ('Descripcion', models.TextField()),
                ('Accesibilidad', models.CharField(max_length=32)),
                ('Telefono', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=20)),
                ('Num_Comentario', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Texto', models.TextField()),
                ('Aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=32)),
                ('Contraseña', models.CharField(max_length=32)),
                ('Titulo_pagina', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='fecha',
            name='Usuario',
            field=models.ForeignKey(to='aparcamientos.Usuario'),
        ),
    ]
