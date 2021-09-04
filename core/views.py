from django.shortcuts import render, redirect
from core.models import *

def lista_eventos(request):
	user = request.user
	# evento = Eventos.objects.get(id=1)
	# eventos = Eventos.objects.all()
	eventos = Eventos.objects.filter(usuario=user)
	return render(request, 'agenda.html', {'eventos':eventos})

def index(request):
	return redirect('/agenda')