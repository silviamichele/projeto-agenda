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
	return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
	if request.POST:
		titulo = request.POST.get('titulo')
		data_evento = request.POST.get('data_evento')
		descricao = request.POST.get('descricao')
		usuario = request.user
		local = request.POST.get('local')
		Eventos.objects.create(titulo=titulo, 
			data_evento=data_evento, 
			descricao=descricao,
			usuario=usuario)

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