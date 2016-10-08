from django.contrib import admin

from .models import Armamento,Reserva,Municao,Acessorio,Militar,Cautela

class CautelaInline(admin.StackedInline):
    model = Cautela
    extra = 1

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

class MunicaoAdmin(admin.ModelAdmin):
    fields = ['descricao','calibre']
    list_display = ('descricao','calibre')
    list_filter = ['calibre']
    search_fields = ['descricao','calibre']

class AcessorioAdmin(admin.ModelAdmin):
    fields = ['descricao']
    search_fields = ['descricao']

class MilitarAdmin(admin.ModelAdmin):
    fields = ['posto','nome_de_guerra','reserva']
    list_display = ('posto','nome_de_guerra')
    search_fields = ['posto','nome_de_guerra']
    list_filter = ['posto']
    inlines = [CautelaInline]


admin.site.register(Armamento,ArmamentoAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Municao,MunicaoAdmin)
admin.site.register(Acessorio,AcessorioAdmin)
admin.site.register(Militar,MilitarAdmin)
admin.site.register(Cautela)
