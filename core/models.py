from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Eventos(models.Model):
	titulo = models.CharField(max_length=200)
	descricao = models.TextField(blank=True)
	data_evento = models.DateTimeField(verbose_name="Data do Evento")
	data_criacao = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	local = models.CharField(max_length=250, blank=True)
	class Meta: 
		db_table = 'evento'

	def __str__(self):
		return self.titulo

	def get_data_evento(self):
		return self.data_evento.strftime('%d/%m/%Y')

	def get_data_input_evento(self):
		return self.data_evento.strftime('%Y-%m-%d')

	def get_evento_atrasado(self):
		if self.data_evento < datetime.now():
			return True
		else:
			return False
	
	def get_evento_proximo(self):
		proximo = datetime.now() + timedelta(days=2)
		anterior = datetime.now()
		if self.data_evento >= anterior and self.data_evento<=proximo:
			return True
		else:
			return False