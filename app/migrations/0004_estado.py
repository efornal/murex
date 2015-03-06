# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_impresora'),
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
    ]
