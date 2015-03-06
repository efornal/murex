# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_oficina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('oficina', models.ForeignKey(to='app.Oficina', null=True)),
            ],
            options={
                'db_table': 'impresoras',
                'verbose_name_plural': 'Impresoras',
            },
            bases=(models.Model,),
        ),
    ]
