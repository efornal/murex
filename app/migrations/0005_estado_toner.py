# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoToner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField(null=True, blank=True)),
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
            name='Toner',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('identificador', models.CharField(max_length=200)),
                ('estados', models.ManyToManyField(to='app.Estado', through='app.EstadoToner')),
                ('impresora', models.ForeignKey(blank=True, to='app.Impresora', null=True)),
                ('proveedor', models.ForeignKey(blank=True, to='app.Proveedor', null=True)),
            ],
            options={
                'db_table': 'toners',
                'verbose_name_plural': 'Toners',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estadotoner',
            name='toner',
            field=models.ForeignKey(to='app.Toner'),
            preserve_default=True,
        ),
    ]
