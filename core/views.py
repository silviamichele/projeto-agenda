from django.shortcuts import render, redirect
from core.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

def login_user(request):
	return render(request, 'login.html')

@login_required(login_url='/login/')
def lista_eventos(request):
	user = request.user
	data_atual = datetime.now()
	# evento = Eventos.objects.get(id=1)
	# eventos = Eventos.objects.all()
	eventos = Eventos.objects.filter(usuario=user, data_evento__gt=data_atual)
	#__lt ultimos eventos, data_evento__gt=data_atual
	dados = {
		'eventos':eventos,
	}
	return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def historico(request):
	data_atual = datetime.now()
	usuario = request.user
	eventos = Eventos.objects.filter(usuario=usuario, data_evento__lt=data_atual)
	return render(request, 'historico.html', {'eventos':eventos})

@login_required(login_url='/login/')
def json_lista_eventos(request):
	user = request.user
	eventos = Eventos.objects.filter(usuario=user).values('id', 'titulo', 'data_evento')
	return JsonResponse(list(eventos), safe=False)

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
	try:
		evento = Eventos.objects.get(id=id_evento)
	except Exception:
		raise Http404()
	if usuario == evento.usuario:
		evento.delete()
	else:
		raise Http404()
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

def criar_usuario(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		first_name = request.POST.get('first_name')
		usuario = User(username=username, password=password, first_name=first_name)
		usuario.set_password(password)
		usuario.save()
		return redirect('/login/')

	else:
		return render(request, 'create_user.html')
