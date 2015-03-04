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
                ('estados', models.ManyToManyField(to='app.Estado')),
                ('proveedor', models.ForeignKey(to='app.Proveedor', null=True)),
            ],
            options={
                'db_table': 'toners',
                'verbose_name_plural': 'Toners',
            },
            bases=(models.Model,),
        ),
    ]
