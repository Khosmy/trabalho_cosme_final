# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentoCosme', '0003_auto_20150519_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='Numero',
            field=models.CharField(max_length=10, verbose_name=b'Vaga'),
        ),
    ]
