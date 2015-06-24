#-*- encoding: utf-8 -*-

from django import forms
from models import Cliente
from models import Carro
from models import Vaga
from models import Alugar

#Create your forms here.

class ClienteForm (forms.modelForm):
	class meta:
		model = Cliente
		fields = ['Nome','Endereço','Número','Bairro','CPF','Contato']

class CarroForm (forms.modelForm):
	class meta:
		model = Carro
		fields = ['Nome','Modelo','Placa','Cor']

class VagaForm (forms.modelForm):
	class meta:
		model = Vaga
		fields = ['Vaga']

class AlugarForm (forms.modelForm):
	class meta:
		model = Alugar
		fields = ['Vaga','Carro','Cliente','Data e Hora','Valor']

