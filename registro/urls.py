from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<equip_reserva_id>[0-9]+)/$', views.shows_equip_reserva_num, name='shows_equip_reserva_id'),
]

