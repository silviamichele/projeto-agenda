from django.contrib import admin
from core.models import Eventos

class EventosAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'data_evento', 'data_criacao')
	list_filter = ('usuario', 'data_evento',)

admin.site.register(Eventos, EventosAdmin)