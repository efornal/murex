# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_estado_toner'),
    ]

    operations = [
        migrations.AddField(
            model_name='toner',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
