# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from .models import Armamento, Municao, Acessorio, Militar, Reserva, Cautela_Armamento, Cautela_Municao, Cautela_Acessorio, Cautela_Militar, Reserva_Armamento, Reserva_Municao, Reserva_Acessorio
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.db import transaction
from datetime import datetime
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


@login_required(login_url="../admin/login/")
def cautelar_index(request):

    #militar = models.ForeignKey('Militar',blank=True,null=True)
    militar_resp = Militar.objects.raw("SELECT * FROM registro_militar WHERE user_id = "+str(request.user.id))[0]
    #reserva = Reserva.objects.all()
    militares = Militar.objects.raw('SELECT id, nome_de_guerra FROM registro_militar')
    armamento = Armamento.objects.raw(
        'SELECT RA.id, (RA.id||" - "||modelo||" - "||fabricante||" - "||numero_de_serie) as name, RRA.reserva_id FROM registro_armamento RA \
        JOIN registro_reserva_armamento RRA WHERE RA.id = RRA.armamento_id'
    )
    municao = Municao.objects.all()
    acessorio = Acessorio.objects.all()


    #return HttpResponse(armamento.name)

    context = {
        'militares': militares,
        'militar_resp': militar_resp,
        'armamento': armamento,
        'municao': municao,
        'acessorio': acessorio,
    }

    template = loader.get_template('registro/cautelar.html')
    return HttpResponse(template.render(context, request))


@transaction.atomic
def formularioCautela(request):
    #salva ponto para possível rollback later
    sid = transaction.savepoint()

    post = request.POST
    #return HttpResponse(post.get('cautela_armamento_id', ''))

    #foreign Models
    militar_cautela = Militar.objects.get(pk=post.get('cautela_militar_cautela', ''))
    militar_resp = Militar.objects.get(pk=post.get('cautela_militar_resp_id', ''))

    reserva_arma_raw = None
    if post.get('cautela_armamento_id', '') != '':
        armamento = Armamento.objects.get(pk=post.get('cautela_armamento_id', ''))

        cautela_armamento = Cautela_Armamento()
        cautela_armamento.data_de_retirada = post.get('cautela_data_retirada', '') +' '+ post.get('cautela_horario_retirada', '')
        cautela_armamento.militar = militar_cautela
        cautela_armamento.armamento = armamento
        cautela_armamento.quantidade = int(post.get('cautela_armamento_quantidade', ''))

        reserva_arma_raw = Reserva.objects.raw("SELECT id FROM registro_reserva_armamento WHERE armamento_id = "+str(post.get('cautela_armamento_id', '')))

        if list(reserva_arma_raw):
            r_reserva_arma = reserva_arma_raw[0]
            reserva_armamento = Reserva_Armamento.objects.get(pk=r_reserva_arma.id)
            reserva_armamento.quantidade = int(reserva_armamento.quantidade) - int(post.get('cautela_armamento_quantidade', ''))
            reserva_armamento.save()
            cautela_armamento.save()

    reserva_muni_raw = None
    if post.get('cautela_municao_id','') != '':
        municao = Municao.objects.get(pk=post.get('cautela_municao_id', ''))

        cautela_municao = Cautela_Armamento()
        cautela_municao.data_de_retirada = post.get('cautela_data_retirada', '') + ' '+post.get('cautela_horario_retirada', '')
        cautela_municao.militar = militar_cautela
        cautela_municao.municao= municao
        cautela_municao.quantidade = post.get('cautela_municao_quantidade', '')

        reserva_muni_raw = Reserva.objects.raw("SELECT id FROM registro_reserva_municao WHERE municao_id ="+str(post.get('cautela_municao_id', '')))
        if list(reserva_muni_raw):
            r_reserva_muni = reserva_muni_raw[0]
            reserva_municao = Reserva_Municao.objects.get(pk=r_reserva_muni.id)
            reserva_municao.quantidade = int(reserva_municao.quantidade) - int(post.get('cautela_municao_quantidade', ''))
            reserva_municao.save()
            cautela_municao.save()

    reserva_acesso_raw = None
    if post.get('cautela_acessorio_id','') != '':
        acessorio = Acessorio.objects.get(pk=post.get('cautela_acessorio_id', ''))

        cautela_acessorio = Cautela_Acessorio()
        cautela_acessorio.data_de_retirada = post.get('cautela_data_retirada', '') +' '+ post.get('cautela_horario_retirada', '')
        cautela_acessorio.militar = militar_cautela
        cautela_acessorio.acessorio = acessorio
        cautela_acessorio.quantidade = post.get('cautela_acessorio_quantidade', '')

        reserva_acesso_raw = Reserva.objects.raw("SELECT id FROM registro_reserva_acessorio WHERE acessorio_id ="+str(post.get('cautela_acessorio_id', '')))
        if list(reserva_acesso_raw):
            r_reserva_acesso = reserva_acesso_raw[0]
            reserva_acessorio = Reserva_Acessorio.objects.get(pk=r_reserva_acesso.id)
            reserva_acessorio.quantidade = int(reserva_acessorio.quantidade) - int(post.get('cautela_acessorio_quantidade', ''))
            reserva_acessorio.save()
            cautela_acessorio.save()

    cautela_militar = Cautela_Militar()
    cautela_militar.militar = militar_cautela
    cautela_militar.militar_resp = militar_resp
    cautela_militar.save()

    transaction.savepoint_commit(sid)
    transaction.atomic()
    template = loader.get_template('registro/cautelar.html')
    context = {
        'save': "Cautela realizada com sucesso",
    }
    #return HtppResponseRedirect('/p_registro/cautelas')
    return HttpResponse(template.render(context, request))
