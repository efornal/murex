# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_proveedor'),
    ]

    operations = [
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
    ]
