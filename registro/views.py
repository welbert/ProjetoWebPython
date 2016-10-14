# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from .models import Armamento, Municao, Acessorio
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.

@login_required(login_url="../admin/login/")
def index(request):
    template = loader.get_template('registro/index.html')
    return HttpResponse(template.render(request))


@login_required(login_url="../admin/login/")
def listar(request):
    #return HttpResponse( "This is a test index" );
    template = loader.get_template('registro/listar.html')

    armamento_list = Armamento.objects.order_by('id')
    municao_list = Municao.objects.order_by('id')
    acessorio_list= Acessorio.objects.order_by('id')

    armamento_count = Armamento.objects.count()
    municao_count= Municao.objects.count()
    acessorio_count= Acessorio.objects.count()

    context = {
        'armamento_list': armamento_list,
        'armamento_count': armamento_count,
        'municao_list': municao_list,
        'municao_count': municao_count,
        'acessorio_list': acessorio_list,
        'acessorio_count': acessorio_count
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="../admin/login/")
def list_arma(request):
    template = loader.get_template('registro/listar.html')

    armamento_list = Armamento.objects.order_by('id')
    armamento_count = Armamento.objects.count()

    context = {
        'armamento_list': armamento_list,
        'armamento_count': armamento_count,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="../admin/login/")
def list_muni(request):
    template = loader.get_template('registro/listar.html')

    municao_list = Municao.objects.order_by('id')

    municao_count= Municao.objects.count()

    context = {
        'municao_list': municao_list,
        'municao_count': municao_count,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="../admin/login/")
def list_acesso(request):
    template = loader.get_template('registro/listar.html')

    acessorio_list = Acessorio.objects.order_by('id')

    acessorio_count= Acessorio.objects.count()

    context = {
        'acessorio_list': acessorio_list,
        'acessorio_count': acessorio_count,
    }
    return HttpResponse(template.render(context, request))

def shows_equip_reserva_num(request, equip_reserva_id):
    #response = "You can see here number of each type of equipament/armament you have in the storage (reserva) %s"

    #model Armamentos
    armamento_list = Armamento.objects.order_by('-id')
    output = "<b>Armamentos</b>"
    output += "<br>"
    i = 0
    for armam in armamento_list:
        i+=1
        output += '<br>'+str(armam.fabricante)+' | '+str(armam.modelo)+' | '+str(armam.numero_de_serie)
    output += "<br><br> Existem <b> %s </b> Armamentos registrados" % i

    #model municao
    municao_list = Municao.objects.order_by('-id')
    output += "<br><br>"
    output += "<b>Munições</b>"
    output += "<br>"
    im = 0
    for item in municao_list:
        im+=1
        output += '<br>'+str(item.calibre)+' | '+str(item.descricao)
    output += "<br><br> Existem <b> %s </b> Munições registradas" % im

    #model acessorio
    acessorio_list = Acessorio.objects.order_by('-id')
    output += "<br><br>"
    output += "<b>Acessorios</b>"
    output += "<br>"
    ia = 0
    for item in acessorio_list:
        ia+=1
        output += '<br>'+str(item.descricao)
    output += "<br><br> Existem <b> %s </b> Acessorios registrados" % ia

    #output += '<br> '.join([(armam.modelo, armam.fabricante) for armam in armamento_list])
    #return HttpResponse( response % equip_reserva_id )

    output += "<br><br><b> Total de equipamentos cadastrados: "+str(i+im+ia)+'<b>'

    return HttpResponse( output )
