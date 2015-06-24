# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentoCosme', '0002_carro_vaga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tempo', models.DateTimeField(null=True, verbose_name=b'Data e Hora')),
                ('Valor', models.DecimalField(null=True, verbose_name=b'Valor', max_digits=20, decimal_places=2)),
                ('Carro', models.ForeignKey(to='estacionamentoCosme.Carro', null=True)),
                ('Cliente', models.ForeignKey(to='estacionamentoCosme.Cliente', null=True)),
                ('Vaga', models.ForeignKey(to='estacionamentoCosme.Vaga', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='Carro',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='Tempo',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='Valor',
        ),
        migrations.AddField(
            model_name='vaga',
            name='Numero',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Vaga'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Contato',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Contato'),
        ),
    ]