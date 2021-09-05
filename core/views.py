from django.shortcuts import render, redirect
from core.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
	return render(request, 'login.html')

@login_required(login_url='/login/')
def lista_eventos(request):
	user = request.user
	# evento = Eventos.objects.get(id=1)
	# eventos = Eventos.objects.all()
	eventos = Eventos.objects.filter(usuario=user)
	return render(request, 'agenda.html', {'eventos':eventos})

@login_required(login_url='/login/')
def evento(request):
	id_evento = request.GET.get('id')
	dados = {}
	if id_evento:
		dados['evento'] = Eventos.objects.get(id=id_evento)
	return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
	if request.POST:
		titulo = request.POST.get('titulo')
		data_evento = request.POST.get('data_evento')
		descricao = request.POST.get('descricao')
		usuario = request.user
		local = request.POST.get('local')
		id_evento = request.POST.get('id')
		if id_evento:
			evento = Eventos.objects.get(id=id_evento)
			if evento.usuario == request.user:
				evento.data_evento=data_evento
				evento.titulo=titulo
				evento.local=local
				evento.descricao=descricao
				evento.save()
			# Eventos.objects.filter(id=id_evento).update(data_evento=data_evento,
			#  	titulo=titulo, 
			#  	local=local, 
			# 	descricao=descricao)
		else:
			Eventos.objects.create(titulo=titulo, 
					data_evento=data_evento, 
					descricao=descricao,
					usuario=usuario)

	return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
	usuario = request.user
	evento = Eventos.objects.get(id=id_evento)
	if usuario == evento.usuario:
		evento.delete()
	return redirect('/')

def index(request):
	return redirect('/agenda')

def login_submit(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		usuario = authenticate(username=username, password=password)

		if usuario is not None:
			login(request, usuario)
			return redirect('/')
		else:
			messages.error(request, 'Usuário ou senha inválido.')
	
	return redirect('/')

def logout_user(request):
	logout(request)
	return redirect('/')