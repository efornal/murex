# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=200, null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'proveedores',
                'verbose_name_plural': 'Proveedores',
            },
            bases=(models.Model,),
        ),
    ]
