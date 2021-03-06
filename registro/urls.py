from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^p_registro/listar_equipamentos', views.listar, name='listar'),
    url(r'^p_registro/armamento', views.list_arma, name='armamento'),
    url(r'^p_registro/municao', views.list_muni, name='municao'),
    url(r'^p_registro/acessorio', views.list_acesso, name='acessorio'),
    url(r'^p_registro/listar_cautelas', views.cautelar_listar, name='listar_cautelas'),
    url(r'^p_registro/cautelas', views.cautelar_index, name='cautelas'),
    url(r'^p_registro/devolver', views.devolver, name='devolver'),
    url(r'^cautelaRegistro', views.formularioCautela, name='formularioCautela'),
    url(r'^(?P<equip_reserva_id>[0-9]+)/$', views.shows_equip_reserva_num, name='shows_equip_reserva_id'),
]

