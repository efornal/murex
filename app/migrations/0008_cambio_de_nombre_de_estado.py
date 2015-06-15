# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_toner_recargas'),
    ]

    operations = [
        migrations.RunSQL("UPDATE estados set nombre='En garantía' WHERE id=5;",
                          "UPDATE estados SET nombre='En devolución' WHERE id=5;"),
    ]
