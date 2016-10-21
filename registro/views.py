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
def cautelar_listar(request):
    #return HttpResponse( "This is a test index" );
    template = loader.get_template('registro/listar_cautelas.html')

    armamento_list = Cautela_Armamento.objects.raw('\
        SELECT caut_arm.id, (arm.modelo||" - "||arm.numero_de_serie) descricao, caut_arm.quantidade, mili.nome_de_guerra, caut_arm.data_de_retirada FROM registro_cautela_armamento caut_arm\
        JOIN registro_reserva_armamento r_arm ON r_arm.id = caut_arm.reserva_armamento_id\
        JOIN registro_armamento arm ON arm.id = r_arm.armamento_id\
        JOIN registro_militar mili ON mili.id = caut_arm.militar_id\
    ')

    municao_list = Cautela_Municao.objects.raw('\
        SELECT caut_muni.id, muni.descricao, caut_muni.quantidade, mili.nome_de_guerra, caut_muni.data_de_retirada FROM registro_cautela_municao caut_muni\
        JOIN registro_reserva_municao r_muni ON r_muni.id = caut_muni.reserva_municao_id\
        JOIN registro_municao muni ON muni.id = r_muni.municao_id\
        JOIN registro_militar mili ON mili.id = caut_muni.militar_id\
    ')

    acessorio_list= Cautela_Acessorio.objects.raw('\
        SELECT caut_acess.id, acess.descricao, caut_acess.quantidade, mili.nome_de_guerra, caut_acess.data_de_retirada FROM registro_cautela_acessorio caut_acess\
        JOIN registro_reserva_acessorio r_acess ON r_acess.id = caut_acess.reserva_acessorio_id\
        JOIN registro_acessorio acess ON acess.id = r_acess.acessorio_id\
        JOIN registro_militar mili ON mili.id = caut_acess.militar_id\
    ')

    armamento_count = Cautela_Armamento.objects.count()
    municao_count= Cautela_Municao.objects.count()
    acessorio_count= Cautela_Acessorio.objects.count()

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
def cautelar_index(request):

    #militar = models.ForeignKey('Militar',blank=True,null=True)
    militar_resp = Militar.objects.raw("SELECT * FROM registro_militar WHERE user_id = "+str(request.user.id))[0]
    #reserva = Reserva.objects.all()
    militares = Militar.objects.raw('SELECT id, nome_de_guerra FROM registro_militar')
    armamento = Armamento.objects.raw(
        'SELECT RRA.id, (modelo||" - "||fabricante||" - "||numero_de_serie) as name, RRA.reserva_id, RR.sigla FROM registro_armamento RA \
        JOIN registro_reserva_armamento RRA ON RA.id = RRA.armamento_id and RRA.quantidade > 0\
        JOIN registro_reserva RR ON RRA.reserva_id = RR.id'
    )
    municao = Municao.objects.raw('SELECT RRM.id, RM.calibre, RM.descricao, RRM.reserva_id, RR.sigla FROM registro_municao RM\
            JOIN registro_reserva_municao RRM ON RRM.municao_id = RM.id and RRM.quantidade > 0\
            JOIN registro_reserva RR ON RRM.reserva_id = RR.id')
    #municao = Municao.objects.all()

    acessorio = Acessorio.objects.raw('SELECT RRAc.id, RAc.descricao, RRAc.reserva_id, RR.sigla FROM registro_acessorio RAc\
        JOIN registro_reserva_acessorio RRAc ON RRAc.acessorio_id = RAc.id and RRAc.quantidade > 0\
        JOIN registro_reserva RR ON RRAc.reserva_id = RR.id')

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


@login_required(login_url="../admin/login/")
@transaction.atomic
def formularioCautela(request):
    #salva ponto para possível rollback later
    sid = transaction.savepoint()
    save = None

    post = request.POST

    #foreign Models
    militar_cautela = Militar.objects.get(pk=post.get('cautela_militar_cautela', ''))
    militar_resp = Militar.objects.get(pk=post.get('cautela_militar_resp_id', ''))

    if post.get('cautela_armamento_id', '') != '' and int(post.get('cautela_armamento_quantidade', '')) > 0:
        reserva_armamento = Reserva_Armamento.objects.get(pk=post.get('cautela_armamento_id', ''))

        cautela_armamento = Cautela_Armamento()
        cautela_armamento.data_de_retirada = post.get('cautela_data_retirada', '') +' '+ post.get('cautela_horario_retirada', '')
        cautela_armamento.militar = militar_cautela
        cautela_armamento.reserva_armamento = reserva_armamento
        cautela_armamento.quantidade = int(post.get('cautela_armamento_quantidade', ''))

        if(int(reserva_armamento.quantidade) >= int(cautela_armamento.quantidade)):
            reserva_armamento.quantidade = int(reserva_armamento.quantidade) - int(post.get('cautela_armamento_quantidade', ''))
            reserva_armamento.save()
            cautela_armamento.save()
            save = 1
        else:
            save = 0

    if post.get('cautela_municao_id','') != '' and int(post.get('cautela_municao_quantidade', '')) > 0:
        reserva_municao = Reserva_Municao.objects.get(pk=post.get('cautela_municao_id', ''))

        cautela_municao = Cautela_Municao()
        cautela_municao.data_de_retirada = post.get('cautela_data_retirada', '') + ' '+post.get('cautela_horario_retirada', '')
        cautela_municao.militar = militar_cautela
        cautela_municao.reserva_municao = reserva_municao
        cautela_municao.quantidade = post.get('cautela_municao_quantidade', '')

        if(int(reserva_municao.quantidade) >= int(cautela_municao.quantidade)):
            reserva_municao.quantidade = int(reserva_municao.quantidade) - int(post.get('cautela_municao_quantidade', ''))
            reserva_municao.save()
            cautela_municao.save()
            save = 1
        else:
            save = 0

    if post.get('cautela_acessorio_id','') != '' and int(post.get('cautela_acessorio_quantidade', '')) > 0:
        reserva_acessorio = Reserva_Acessorio.objects.get(pk=post.get('cautela_acessorio_id', ''))

        cautela_acessorio = Cautela_Acessorio()
        cautela_acessorio.data_de_retirada = post.get('cautela_data_retirada', '') +' '+ post.get('cautela_horario_retirada', '')
        cautela_acessorio.militar = militar_cautela
        cautela_acessorio.reserva_acessorio = reserva_acessorio
        cautela_acessorio.quantidade = post.get('cautela_acessorio_quantidade', '')

        if( int(reserva_acessorio.quantidade) >= int(cautela_acessorio.quantidade)):
            reserva_acessorio.quantidade = int(reserva_acessorio.quantidade) - int(post.get('cautela_acessorio_quantidade', ''))
            reserva_acessorio.save()
            cautela_acessorio.save()
            save = 1
        else:
            save = 0

    #verifica se foi feito algum save, se não mitiga o erro
    if( save == 1 ):
        cautela_militar = Cautela_Militar()
        cautela_militar.militar = militar_cautela
        cautela_militar.militar_resp = militar_resp
        cautela_militar.save()
    elif(save == None):
        #nenhum save foi setado até o momento. Logo não foi informado item ou quantidade
        save = 2

#    transaction.savepoint_rollback(sid)
    transaction.savepoint_commit(sid)
    transaction.atomic()

    template = loader.get_template('registro/cautelar.html')

    #Gera mensagem de tratamento e redireciona pra pagina template de cautelas
    context = {}

    if( save == 0):
        save = "Erro: Quantidade maior que o disponível na reserva"
    elif( save == 2 ):
        save = "Nenhum item foi selecionado ou quantidade não informada"
    else:
        save = "Cautela realizada com sucesso"
        count_armamento = Cautela_Armamento.objects.raw("\
                SELECT id, COUNT(*) count FROM registro_cautela_armamento WHERE militar_id = "+str(post.get('cautela_militar_cautela', ''))+"\
        ")
        count_municao = Cautela_Municao.objects.raw("\
                SELECT id, COUNT(*) count FROM registro_cautela_municao WHERE militar_id = "+str(post.get('cautela_militar_cautela', ''))+"\
        ")
        count_acessorio = Cautela_Acessorio.objects.raw("\
                SELECT id, COUNT(*) count FROM registro_cautela_acessorio WHERE militar_id = "+str(post.get('cautela_militar_cautela', ''))+"\
        ")

        context = {
            'count': 1,
            'count_armamento' : count_armamento[0].count,
            'count_municao' : count_municao[0].count,
            'count_acessorio' : count_acessorio[0].count,
        }

#        return HttpResponse(count_armamento[0].count)

    context['save'] = save

    #return HtppResponseRedirect('/p_registro/cautelas')
    return HttpResponse(template.render(context, request))

@login_required(login_url="../admin/login/")
@transaction.atomic
def devolver(request):
    template = loader.get_template('registro/devolver.html')

    sid = transaction.savepoint()
    get = request.GET

    c_armamento_id = get.get('carma_id', '')
    c_municao_id = get.get('cmuni_id', '')
    c_acessorio_id = get.get('caces_id', '')

    save = None
    num_devolvido = None
    if c_armamento_id != '':
        cautela_armamento = Cautela_Armamento.objects.get(id=c_armamento_id)
        num_devolvido = cautela_armamento.quantidade

        reserva_armamento = Reserva_Armamento.objects.get(id=cautela_armamento.reserva_armamento_id)
        reserva_armamento.quantidade = reserva_armamento.quantidade + cautela_armamento.quantidade
        reserva_armamento.save()

        cautela_armamento.delete()
        save = 1

    if c_municao_id != '':
        cautela_municao = Cautela_Municao.objects.get(id=c_municao_id)
        num_devolvido = cautela_municao.quantidade

        reserva_municao = Reserva_Municao.objects.get(id=cautela_municao.reserva_municao_id)
        reserva_municao.quantidade = reserva_municao.quantidade + cautela_municao.quantidade
        reserva_municao.save()

        cautela_municao.delete()
        save = 1

    if c_acessorio_id != '':
        cautela_acessorio = Cautela_Acessorio.objects.get(id=c_acessorio_id)
        num_devolvido = cautela_acessorio.quantidade

        reserva_acessorio = Reserva_Acessorio.objects.get(id=cautela_acessorio.reserva_acessorio_id)
        reserva_acessorio.quantidade = reserva_acessorio.quantidade + cautela_acessorio.quantidade
        reserva_acessorio.save()

        cautela_acessorio.delete()
        save = 1

    context = {}
    if save:
        context = {
            'save': 1,
            'num_devolvido': int(num_devolvido),
        }

    if c_armamento_id != '':
        context['count_armamento'] = Cautela_Armamento.objects.raw('\
                SELECT id, count(*) num FROM  registro_cautela_armamento\
                WHERE militar_id = '+str(cautela_armamento.militar_id)+'\
        ')[0].num

        context['militar'] = Militar.objects.get(id=cautela_armamento.militar_id)

    if c_municao_id != '':
        context['count_municao'] = Cautela_Municao.objects.raw('\
                SELECT id, count(*) num FROM  registro_cautela_municao\
                WHERE militar_id = '+str(cautela_municao.militar_id)+'\
        ')[0].num

        context['militar'] = Militar.objects.get(id=cautela_municao.militar_id)

    if c_acessorio_id != '':
        context['count_acessorio'] = Cautela_Acessorio.objects.raw('\
                SELECT id, count(*) num FROM  registro_cautela_acessorio\
                WHERE militar_id = '+str(cautela_acessorio.militar_id)+'\
        ')[0].num

        context['militar'] = Militar.objects.get(id=cautela_acessorio.militar_id)

    #transaction.savepoint_rollback(sid)
    transaction.savepoint_commit(sid)
    transaction.atomic()
    #return HttpResponse(context)
    return HttpResponse(template.render(context, request))
