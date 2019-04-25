from django.contrib import admin
from .models import AreaTematica, Modalidade, Evento, Anais, Trabalho,\
    Afiliacao, Autor

admin.site.register(AreaTematica)
admin.site.register(Modalidade)
admin.site.register(Anais)
admin.site.register(Trabalho)
admin.site.register(Afiliacao)
#admin.site.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'nome_para_citacao', 'afiliacao__sigla']
    list_display = ('nome','afiliacao','contato')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','local','slug')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Evento, EventoAdmin)
