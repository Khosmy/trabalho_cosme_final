__author__ = 'cosme.cardoso'
#coding:utf-8
from django.shortcuts import render,redirect, render_to_response

from forms import *

from models import *

# Create your views here.

def index(request):
	return render_to_response('index.html')

def cliente(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Cliente.objects.filter(Nome__contains=pesquisar)
	else:
		post = Cliente.objects.all()
	return render(request,'cliente.html',{'post': post})

def cadastraCliente(request):
	if codigo == None:
		obj = None
	else:
		obj = get_object_or_404(Cliente,pk = codigo)
	if request.method == 'post':
		form = cadastraClienteForm(request.POST)
		if form.is_valid():
			#q = form.save(commit=False)
			#q.nome = u"TESTE-%s" % q.nome
			#q.save()
			form.save()
			return redirect ('lista_cliente')
	else:
		form = cadastraClienteForm()
	return render(request,"cadastro/form.html",{'form':form})

def EditaCliente(request,codigo=None):
    obj = get_object_or_404(Cliente,pk=codigo)
    if request.method == 'POST':
        form = CadastraClienteForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('edita_cliente')
    else:
        form = CadastraClienteForm(instance=obj)
    return render(request,"cadastro/form.html",{'form':form})

def carro(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Carro.objects.filter(Modelo__contains=pesquisar)
	else:
		post = Carro.objects.all()
	return render(request,'carro.html',{'post': post})

def cadastraCarro(request):
	if codigo == None:
		obj = None
	else:
		obj = get_object_or_404(Carro,pk = codigo)
	if request.method == 'post':
		form = cadastraCarroForm(request.POST)
		if form.is_valid():
			#q = form.save(commit=False)
			#q.nome = u"TESTE-%s" % q.nome
			#q.save()
			form.save()
			return redirect ('lista_carro')
	else:
		form = cadastraCarroForm()
	return render(request,"cadastro/form.html",{'form':form})

def EditaCarro(request,codigo=None):
    obj = get_object_or_404(Carro,pk=codigo)
    if request.method == 'POST':
        form = CadastraCarroForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lista_carro')
    else:
        form = CadastraCarroForm(instance=obj)
    return render(request,"cadastro/form.html",{'form':form})

def vaga(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Vaga.objects.filter(Numero__contains=pesquisar)
	else:
		post = Vaga.objects.all()
	return render(request,'vaga.html',{'post': post})

def cadastraVaga(request):
	if codigo == None:
		obj = None
	else:
		obj = get_object_or_404(Vaga,pk = codigo)
	if request.method == 'post':
		form = cadastraVagaForm(request.POST)
		if form.is_valid():
			#q = form.save(commit=False)
			#q.nome = u"TESTE-%s" % q.nome
			#q.save()
			form.save()
			return redirect ('lista_Vaga')
	else:
		form = cadastraVagaForm()
	return render(request,"cadastro/form.html",{'form':form})

def EditaVaga(request,codigo=None):
    obj = get_object_or_404(Vaga,pk=codigo)
    if request.method == 'POST':
        form = CadastraVagaForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lista_vaga')
    else:
        form = CadastraVagaForm(instance=obj)
    return render(request,"cadastro/form.html",{'form':form}

# request.POST.get('pesquisar')
		post = Alugar.objects.filter(Cliente__contains=pesquisar)
	else:
		post = Alugar.objects.all()
	return render(request,'Alugar.html',{'post': post})

def cadastraAlugar(request):
	if codigo == None:
		obj = None
	else:
		obj = get_object_or_404(Alugar,pk = codigo)
	if request.method == 'post':
		form = cadastraAlugarForm(request.POST)
		if form.is_valid():
			#q = form.save(commit=False)
			#q.nome = u"TESTE-%s" % q.nome
			#q.save()
			form.save()
			return redirect ('lista_Alugar')
	else:
		form = cadastraAlugarForm()
	return render(request,"cadastro/form.html",{'form':form})

def EditaAlugar(request,codigo=None):
    obj = get_object_or_404(Alugar,pk=codigo)
    if request.method == 'POST':
        form = CadastraAlugarForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lista_alugar')
    else:
        form = CadastraAlugarForm(instance=obj)
    return render(request,"cadastro/form.html",{'form':form}