# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentoCosme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Modelo', models.CharField(max_length=100, null=True, verbose_name=b'Modelo')),
                ('Marca', models.CharField(max_length=100, null=True, verbose_name=b'Marca')),
                ('Placa', models.CharField(max_length=10, null=True, verbose_name=b'Placa')),
                ('Cor', models.CharField(max_length=20, null=True, verbose_name=b'Cor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tempo', models.DateTimeField(null=True, verbose_name=b'Data e Hora')),
                ('Valor', models.DecimalField(null=True, verbose_name=b'Valor', max_digits=20, decimal_places=2)),
                ('Carro', models.ForeignKey(to='estacionamentoCosme.Carro', null=True)),
                ('Cliente', models.ForeignKey(to='estacionamentoCosme.Cliente', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
