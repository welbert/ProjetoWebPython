from django.contrib import admin

from .models import Armamento,Reserva,Municao,Acessorio,Militar

class ArmamentoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['numero_de_serie']}),
        ('Informacoes', {'fields': ['modelo','fabricante']}),
    ]
    list_display = ('numero_de_serie', 'modelo','fabricante')
    list_filter = ['numero_de_serie', 'modelo','fabricante']
    search_fields = ['modelo','fabricante']

class ReservaAdmin(admin.ModelAdmin):
    fields = ['sigla','descricao']
    list_display = ('sigla', 'descricao')
    search_fields = ['sigla','descricao']

admin.site.register(Armamento,ArmamentoAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Municao)
admin.site.register(Acessorio)
admin.site.register(Militar)
