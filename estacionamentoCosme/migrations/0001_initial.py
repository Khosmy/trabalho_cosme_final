# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endere\xc3\xa7o')),
                ('Numero', models.IntegerField(max_length=10,null=True, verbose_name=b'N\xc3\xbamero')),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cpf', models.CharField(max_length=11, null=True, verbose_name=b'CPF')),
                ('Contato', models.CharField(max_length=15, null=True, verbose_name=b'Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
