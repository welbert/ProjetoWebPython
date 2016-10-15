from django.contrib import admin

from .models import Armamento,Reserva,Municao,Acessorio,Militar,Cautela_Acessorio,Cautela_Municao,Cautela_Armamento,Reserva_Armamento,Reserva_Municao,Reserva_Acessorio

class CautelaAcessorioInline(admin.StackedInline):
    model = Cautela_Acessorio
    extra = 0

class CautelaMunicaoInline(admin.StackedInline):
    model = Cautela_Municao
    extra = 0

class CautelaArmamentoInline(admin.StackedInline):
    model = Cautela_Armamento
    extra = 0

class ReservaAcessorioInline(admin.StackedInline):
    model = Reserva_Acessorio
    extra = 0

class ReservaMunicaoInline(admin.StackedInline):
    model = Reserva_Municao
    extra = 0

class ReservaArmamentoInline(admin.StackedInline):
    model = Reserva_Armamento
    extra = 0

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
    inlines = [ReservaAcessorioInline,ReservaMunicaoInline,ReservaArmamentoInline]

class MunicaoAdmin(admin.ModelAdmin):
    fields = ['descricao','calibre']
    list_display = ('descricao','calibre')
    list_filter = ['calibre']
    search_fields = ['descricao','calibre']

class AcessorioAdmin(admin.ModelAdmin):
    fields = ['descricao']
    search_fields = ['descricao']

class MilitarAdmin(admin.ModelAdmin):
    fields = ['posto','nome_de_guerra','reserva','user']
    list_display = ('posto','nome_de_guerra')
    search_fields = ['posto','nome_de_guerra']
    list_filter = ['posto']
    inlines = [CautelaAcessorioInline,CautelaMunicaoInline,CautelaArmamentoInline]


admin.site.register(Armamento,ArmamentoAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Municao,MunicaoAdmin)
admin.site.register(Acessorio,AcessorioAdmin)
admin.site.register(Militar,MilitarAdmin)
