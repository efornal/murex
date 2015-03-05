# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'estados',
                'verbose_name_plural': 'Estados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstadoToner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('recargado', models.BooleanField(default=False)),
                ('estado', models.ForeignKey(to='app.Estado')),
            ],
            options={
                'db_table': 'estados_toners',
                'verbose_name_plural': 'EstadosToners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'impresoras',
                'verbose_name_plural': 'Impresoras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'oficinas',
                'verbose_name_plural': 'Oficinas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
            ],
            options={
                'db_table': 'proveedores',
                'verbose_name_plural': 'Preoveedores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Toner',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('identificador', models.CharField(max_length=200)),
                ('estados', models.ManyToManyField(to='app.Estado', through='app.EstadoToner')),
                ('impresora', models.ForeignKey(to='app.Impresora', null=True)),
                ('proveedor', models.ForeignKey(to='app.Proveedor', null=True)),
            ],
            options={
                'db_table': 'toners',
                'verbose_name_plural': 'Toners',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='impresora',
            name='oficina',
            field=models.ForeignKey(to='app.Oficina', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estadotoner',
            name='toner',
            field=models.ForeignKey(to='app.Toner'),
            preserve_default=True,
        ),
    ]
