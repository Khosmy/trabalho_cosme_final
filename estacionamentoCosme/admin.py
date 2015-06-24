#-*- encoding: utf-8 -*-
from django.contrib import admin
from estacionamentoCosme.models import Cliente, Carro, Vaga, Alugar


class ClienteAdmin(admin.ModelAdmin):
	list_display = ['Nome','Endereco','Numero','Bairro','Cpf','Contato']
	list_filter = ['Nome']
	search_fields = ['Nome']

class CarroAdmin(admin.ModelAdmin):
	list_display = ['Modelo','Marca','Placa','Cor']
	list_filter = ['Placa']
	search_fields = ['Placa','Modelo']

class VagaAdmin(admin.ModelAdmin):
	list_display = ['Numero']
	search_fields = ['Numero']

class AlugarAdmin(admin.ModelAdmin):
	list_display = ['Vaga','Carro','Cliente','Tempo','Valor']
	list_filter = ['Carro','Cliente']
	search_fields = ['Carro','Cliente']

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Vaga)
admin.site.register(Alugar)

